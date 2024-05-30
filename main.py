import os
import serial
import threading
import time
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from serial.serialutil import SerialException

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WFN238w03vnlSO439gown44'
db_file = os.path.join(os.getcwd(), 'temperature.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_file}'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
serial_port = None
try:
    serial_port = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
except SerialException:
    print("No device is connected")

import api_routes
from user import User
from Temperature import Temperature


@login_manager.unauthorized_handler
def handler():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("login attempt")
        login = request.form['login']
        password = request.form['password']
        user = User.query.filter_by(login=login).first()
        if user and bcrypt.check_password_hash(user.hash, password):
            login_user(user, remember=True)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')


@app.route('/registration', methods=['GET','POST'])
def registration():
    if request.method == 'POST':
        print("registration attempt")
        username = request.form['login']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password)
        user = User(login=username, hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created for {0}!'.format(username), 'success')
        return redirect(url_for('login'))

    return render_template('registration.html')


@login_required
@app.route('/dashboard')
def dashboard():
    if not current_user.is_authenticated:
        redirect(url_for('login'))
    print(f'Username: {current_user.login}')
    return render_template("dashboard.html", user=current_user.login)


@login_required
@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return redirect("/dashboard")


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def read_serial_and_write_to_db():
    with app.app_context():
        while True:
            try:
                # Read the temperature value from the serial port
                line = serial_port.readline().strip()
                if line:
                    temperature_value = float(line)

                    # Store the temperature value in the database
                    timestamp = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime())
                    temperature_entry = Temperature(value=temperature_value, timestamp=timestamp)
                    db.session.add(temperature_entry)
                    db.session.commit()

                    print(f'Temperature value {temperature_value} recorded.')
                else:
                    print('No data read from serial port')
            except ValueError:
                print('Invalid data received from serial port')
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    if serial_port is not None:
        threading.Thread(target=read_serial_and_write_to_db, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
