from __main__ import app
from data import Data

data = Data()


# Vložení hodnoty {“timestamp”: value, “temp”: value}
@app.route('/api/add/<value>', methods=['POST'])
def add(value):
    data.add(value)
    return data.temps


# Získání poslední hodnoty {“timestamp”: value, “temp”: value}

@app.route('/api/last/')
def last():
    return data.last()


# Získání posledních X naměřených hodnot.

@app.route('/api/last/<n>')
def last_n(n):
    return data.last_n(n)


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