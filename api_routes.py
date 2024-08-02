from __main__ import app
import json
from data import Data
from flask import request, jsonify, Response

data = Data()


# Vložení hodnoty {“timestamp”: value, “temp”: value}
@app.route('/api/add/<value>', methods=['POST', 'GET'])
def add(value):
    data.add(float(value))
    last_record = data.last()
    return jsonify(last_record.to_dict())

@app.route('/api/last/', methods=['GET'])
def last():
    last_record = data.last()
    return jsonify(last_record.to_dict())

@app.route('/api/last/<n>', methods=['GET'])
def last_n(n):
    last_n_records = data.last_n(int(n))
    return jsonify([record.to_dict() for record in last_n_records])

@app.route('/api/delete_oldest/<n>', methods=['POST'])
def delete_n(n):
    data.del_n_oldest(int(n))
    all_records = data.get_all()
    return jsonify([record.to_dict() for record in all_records])

@app.route('/api/get_all_temps', methods=['GET'])
def get_all_temps():
    all_records = data.get_all()
    return jsonify([record.to_dict() for record in all_records])

@app.route('/api/delete/<timestamp>', methods=['POST'])
def delete(timestamp):
    remaining_records = data.delete(timestamp)
    return jsonify([record.to_dict() for record in remaining_records])

@app.route("/api/number_of_records", methods=['GET'])
def number_of_records():
    count = data.count()
    return jsonify({'value': count})


# @app.route("/api/register")
# def register():
#     login = request.args.get('login')
#     password = request.args.get('password')