from .conexion_db import Conexiondb
from tkinter import messagebox

def crear_tabla_clientes():
    conexion = Conexiondb()

    sql = '''
    CREATE TABLE clientes 
    ("id"	INTEGER,
	"Nombre"	VARCHAR(50),
	"Apellido"	VARCHAR(50),
	"Fecha_de_Nacimiento"	 DATE,
	"Genero"	VARCHAR(50),
	"Telefono"	VARCHAR(50),
	"Domicilio"	VARCHAR(50),
	"Localidad"	VARCHAR(50),
	"Email"	VARCHAR(50),
	PRIMARY KEY("id" AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_conexion()
        messagebox.showinfo('Configuracion','Tabla CLIENTES creada')
    except:
        messagebox.showwarning('ATENTO','La tabla CLIENTES ya existe')


def crear_tabla_pagos():
    conexion = Conexiondb()

    sql = '''
    CREATE TABLE IF NOT EXISTS pagos 
    ("id"	INTEGER,
	"fecha_movimiento"	DATE,
	"fecha_pago"	DATE,
	"detalle"	VARCHAR(150),
	"monto"	DECIMAL(5, 2),
	"cliente"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
    )
    '''
    conexion.cursor.execute(sql)
    conexion.cerrar_conexion()

def guardar_cliente(cliente):
    conexion = Conexiondb()
    sql = f"""INSERT INTO clientes (Nombre, Apellido, Fecha_de_Nacimiento, Genero, Telefono, Domicilio, Localidad, Email)
    VALUES ('{cliente.Nombre}','{cliente.Apellido}','{cliente.Fecha_de_Nacimiento}','{cliente.Genero}','{cliente.Telefono}','{cliente.Domicilio}','{cliente.Localidad}','{cliente.Email}')
    """
    
    conexion.cursor.execute(sql)
    conexion.cerrar_conexion()
    messagebox.showinfo('Clientes','Cliente Guardado...!')
    


def guardar_pago():
    conexion = Conexiondb()
    sql = '''
    
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_conexion()
        messagebox.showinfo('Pagos','Pago Guardado...!')
    except:
        messagebox.showwarning('ATENTO','Paso algo al guardar el pago')


class Cliente:
    def __init__(self, Nombre, Apellido, Fecha_de_Nacimiento, Genero, Telefono, Domicilio, Localidad, Email ):
        self.id = None
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Fecha_de_Nacimiento = Fecha_de_Nacimiento
        self.Genero = Genero
        self.Telefono = Telefono
        self.Domicilio = Domicilio
        self.Localidad = Localidad
        self.Email = Email

    def __str__(self):
        return f'Cliente[{self.Nombre},{self.Apellido},{self.Fecha_de_Nacimiento},{self.Genero},{self.Telefono},{self.Domicilio},{self.Localidad},{self.Email}]'

    
def mostrar_clientes():
    conexion = Conexiondb()
    lista_clientes = []
    sql = 'SELECT * FROM clientes'
    conexion.cursor.execute(sql)
    lista_clientes = conexion.cursor.fetchall()
    conexion.cerrar_conexion()
    return lista_clientes

def modificar_cliente(idcliente,cliente):
    conexion = Conexiondb()
    sql = f"""UPDATE clientes 
    SET Nombre ='{cliente.Nombre}', 
    Apellido ='{cliente.Apellido}',
    Fecha_de_Nacimiento ='{cliente.Fecha_de_Nacimiento}',
    Genero ='{cliente.Genero}',
    Telefono ='{cliente.Telefono}',
    Domicilio ='{cliente.Domicilio}',
    Localidad ='{cliente.Localidad}',
    Email ='{cliente.Email}'
    WHERE id ={idcliente}
    """
    
    conexion.cursor.execute(sql)
    conexion.cerrar_conexion()
    messagebox.showinfo('Clientes','Cliente editado con exito...!') 


