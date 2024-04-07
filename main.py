from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

username = "username"


@app.route('/<anything>')
def hello_world(anything):  # put application's code here
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template("login.html", user=username)


@app.route('/registration')
def registration():
    return render_template("registration.html", user=username)


@app.route('/dashboard')
def dashboard():
    temp_map = {
        "21-2-2024 13:00:00": 9.5,
        "21-2-2024 18:00:00": 6.5,
        "23-2-2024 13:00:00": 11.0,
        "23-2-2024 18:00:00": 9.3,
        "25-2-2024 13:00:00": 9.9,
        "25-2-2024 18:00:00": 10.7,
        "27-2-2024 13:00:00": 10.3,
        "27-2-2024 18:00:00": 4.3,
        "29-2-2024 13:00:00": 14.7,
        "29-2-2024 18:00:00": 15.3,
        "2-3-2024 13:00:00": 13.9,
        "2-3-2024 18:00:00": 15.4,
        "4-3-2024 13:00:00": 8.6,
        "4-3-2024 18:00:00": 7.7
    }
    temps_number = len(list(temp_map.keys()))
    last_temp = list(temp_map.keys())[len(temp_map) - 1]
    return render_template("dashboard.html", data=temp_map, user=username, last_temp=last_temp, t_number=temps_number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
