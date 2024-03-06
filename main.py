from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<anything>')
def hello_world(anything):  # put application's code here
    return render_template("hello.html")


@app.route('/login')
def login():
    return "<h1>Login</h1>"


@app.route('/registration')
def registration():
    return "<h1>Registration</h1>"


@app.route('/dashboard')
def dashboard():
    temp_map = {
        "21-2-2024": 9.5,
        "23-2-2024": 11.0,
        "25-2-2024": 9.9,
        "27-2-2024": 10.3,
        "29-2-2024": 14.7,
        "2-3-2024": 13.9,
        "4-3-2024": 7.7
    }
    return "<h1>Dashboard</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
