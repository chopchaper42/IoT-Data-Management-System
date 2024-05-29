from __main__ import app
import json
from data import Data
from flask import request, jsonify, Response

data = Data()


# Vložení hodnoty {“timestamp”: value, “temp”: value}
@app.route('/api/add/<value>', methods=['POST', 'GET'])
def add(value):
    data.add(value)
    return jsonify(data.last())


# Získání poslední hodnoty {“timestamp”: value, “temp”: value}

@app.route('/api/last/', methods=['GET'])
def last():
    return Response(json.dumps(data.last().to_json()), mimetype='application/json')


# Získání posledních X naměřených hodnot.

@app.route('/api/last/<n>')
def last_n(n):
    last_n = data.last_n(n)
    return Response(json.dumps(last_n))


# Smazání nejstarších Y naměřených hodnot.

@app.route('/api/delete_oldest/<n>')
def delete_n(n):
    data.del_n_oldest(n)
    return data.temps


# Ziskani vsech hodnot

@app.route('/api/get_all_temps')
def get_all_temps():
    return data.temps


@app.route('/api/delete/<n>')
def delete(n):
    return data.delete(n)


@app.route("/api/number_of_records")
def number_of_records():
    return { "value": len(data.temps) }


@app.route("/api/register")
def register():
    login = request.args.get('login')
    password = request.args.get('password')