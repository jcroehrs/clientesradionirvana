import sqlite3

class Conexiondb:
    def __init__(self):
        self.base_datos = 'database/db.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor =self.conexion.cursor()


    def cerrar_conexion(self):
        self.conexion.commit()
        self.conexion.close()
