from flask import Flask, render_template, redirect, url_for, send_from_directory
from data import Data

app = Flask(__name__, '/static')

import api_routes

username = "username"
data = Data()

# @app.route('/<anything>')
# def hello_world(anything):  # put application's code here
#     return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template("login.html", user=username)


@app.route('/registration')
def registration():
    return render_template("registration.html", user=username)


@app.route('/dashboard')
def dashboard():
    temps_number = len(data.temps)
    last_temp = data.temps[len(data.temps) - 1]
    return render_template("dashboard.html", data=data.temps, user=username, last_temp=last_temp["value"], t_number=temps_number)


if __name__ == '__main__':
    # temp_map = {
    #     "21-2-2024 13:00:00": 9.5,
    #     "21-2-2024 18:00:00": 6.5,
    #     "23-2-2024 13:00:00": 11.0,
    #     "23-2-2024 18:00:00": 9.3,
    #     "25-2-2024 13:00:00": 9.9,
    #     "25-2-2024 18:00:00": 10.7,
    #     "27-2-2024 13:00:00": 10.3,
    #     "27-2-2024 18:00:00": 4.3,
    #     "29-2-2024 13:00:00": 14.7,
    #     "29-2-2024 18:00:00": 15.3,
    #     "2-3-2024 13:00:00": 13.9,
    #     "2-3-2024 18:00:00": 15.4,
    #     "4-3-2024 13:00:00": 8.6,
    #     "4-3-2024 18:00:00": 7.7
    # }
    # new_temps = []
    # for temp in temp_map:
    #     new_temps.append({"timestamp": temp, "temp": temp_map[temp]})
    #
    # with open('temps.json', 'w') as f:
    #     json.dump(new_temps, f)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
