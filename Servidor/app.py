import sqlite3
from flask import Flask, request, g, jsonify

def dict_factory(cursor, row):
 """Arma un diccionario con los valores de la fila."""
 fields = [column[0] for column in cursor.description]
 return {key: value for key, value in zip(fields, row)}



def abrirConexion():
    if 'db' not in g:   # Si todavía no hay conexión
        g.db = sqlite3.connect("sensore.sqlite")  # abre la base
        g.db.row_factory = dict_factory           # hace que las filas se accedan como diccionario
    return g.db



def cerrarConexion(e=None):
    db = g.pop('db', None)   # saca la conexión de g (si existe)
    if db is not None:
        db.close()           # la cierra







app = Flask(__name__)
app.teardown_appcontext(cerrarConexion)


@app.route("/api/sensor/enviar", methods=['POST'])
def valor():
    db=abrirConexion()
    Sensor= request.json['Nombre']
    Valor= request.json['Valor']
    print(f"{Sensor} y {Valor}")
    cerrarConexion()
    return "ok"


@app.route("/api/sensor", methods=['POST'])
def insertar():
    db = abrirConexion()
    data = request.get_json()   # toma el JSON enviado en el POST
    Sensor = data['Nombre']
    Valor = data['Valor']
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO Valores (Nombre, Valor) VALUES (?, ?)',
        (Sensor, Valor)#remplaza los signos ?
    )

    db.commit()  # guarda los cambios en la base
    respuesta = {"repuesta" : "ok"}
    cerrarConexion()
    return jsonify(respuesta)


@app.route("/api/sensor/mostrar")
def mostrar():
    db = abrirConexion()
    resultado = db.execute('SELECT * FROM Valores').fetchall()
    cerrarConexion()
    return resultado
    




