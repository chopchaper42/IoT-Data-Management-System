# Flask application for managing data colected by an IoT device

The project is divided to 5 miniprojects. Each of them adds new functionality. Each miniproject has its own branch in the repository.

## Miniproject 1
The task was to create a simple web page and create an application in Python to serve the page. Datastorage is implemented as a im-memory dictionary.

## Miniproject 2
This miniproject extends the application with REST API.

## Miniproject 3
3rd miniproject swaps a dictionary to a SQLite database. Flask-SQLAlchemy is used as an ORM. Login and Registration are added.

## Miniproject 4
A script in Micropython created for Raspberry Pi Pico WH to generate a random real number every 20 sec and send it to the server's serial port.

## Miniproject 5
This project adds a new way to send data to the server - MQTT.
