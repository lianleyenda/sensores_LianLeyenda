import sqlite3
from flask import Flask, request, g

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


@app.route("/api/sensor", methods=['POST'])
def valor():
    db=abrirConexion()
    Sensor= request.json['Nombre']
    Valor= request.json['Valor']
    print(f"{Sensor} y {Valor}")
    cerrarConexion()
    return "ok"
