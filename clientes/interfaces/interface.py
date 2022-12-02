from tkinter import Tk
from tkinter import ttk
import tkinter as tk

from model.clientes_dao import crear_tabla_clientes, crear_tabla_pagos
from model.clientes_dao import Cliente, guardar_cliente, mostrar_clientes, modificar_cliente


# ******************* MENU *******************

def barra_menu(root):

    barra_menu = tk.Menu(root)
    root.config(bg='#26abbe',menu = barra_menu , width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    menu_inicio.config(bg='#26abbe')
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    menu_inicio.add_command(label='...')
    menu_inicio.add_command(label='...')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Nuevo')
    barra_menu.add_cascade(label='Modificar')

    menu_configuracion = tk.Menu(barra_menu, tearoff=0)
    menu_configuracion.config(bg='#26abbe')
    barra_menu.add_cascade(label='Configuracion', menu=menu_configuracion)
    menu_configuracion.add_command(label='Crear tabla clientes', command=crear_tabla_clientes)
    menu_configuracion.add_command(label='Crear tabla pagos', command=crear_tabla_pagos)

    barra_menu.add_cascade(label='Ayuda')


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=1366, height=778)
        self.root = root
        self.pack()
        self.config(bg='#26abbe')
        self.campos_cliente()
        self.deshabilitar()
        self.tabla_clientes()
        self.id_cli = None
        #f161a7 rosa 
        #26abbe celeste
        #1671aa azul
        #f8ce18 amarillo

    
    def campos_cliente(self):
        #***************** LABELS ***************************
        self.label_nombre = tk.Label(self, text='Nombre :')
        self.label_nombre.config(font=('Arial', 12, 'bold'), bg='#26abbe')
        self.label_nombre.grid(row=1, column=0, padx=2, pady=2)

        self.label_apellido = tk.Label(self, text='Apellido :')
        self.label_apellido.config(font=('Arial', 12, 'bold'), bg='#26abbe')
        self.label_apellido.grid(row=2, column=0, padx=2, pady=2)

        self.label_fnacimiento = tk.Label(self, text='Fecha de nacimiento :')
        self.label_fnacimiento.config(font=('Arial', 12, 'bold'), bg='#26abbe')
        self.label_fnacimiento.grid(row=3, column=0, padx=2 , pady=2)

        self.label_genero = tk.Label(self, text='Genero :')
        self.label_genero.config(font=('Arial', 12, 'bold'), bg='#26abbe')
        self.label_genero.grid(row=4, column=0, padx=2 , pady=2)

        self.label_telefono = tk.Label(self, text='Telefono :')
        self.label_telefono.config(font=('Arial', 12, 'bold'), bg='#26abbe')
        self.label_telefono.grid(row=5, column=0, padx=2, pady=2)

        self.label_domicilio = tk.Label(self, text='Domicilio :')
        self.label_domicilio.config(font=('Arial', 12, 'bold'), bg='#26abbe')
        self.label_domicilio.grid(row=6, column=0, padx=2, pady=2)

        self.label_localidad = tk.Label(self, text='Localidad :')
        self.label_localidad.config(font=('Arial', 12, 'bold'), bg='#26abbe')
        self.label_localidad.grid(row=7, column=0, padx=2, pady=2)

        self.label_email = tk.Label(self, text='Email :')
        self.label_email.config(font=('Arial', 12, 'bold'), bg='#26abbe')
        self.label_email.grid(row=8, column=0, padx=2, pady=2)
        
        
        #***************** ENTRADA DE DATOS ***********************
        self.v_nombre = tk.StringVar()
        self.entrada_nombre = tk.Entry(self, textvariable=self.v_nombre)
        self.entrada_nombre.config(width=50, font=('Arial', 12),bg='green')
        self.entrada_nombre.grid(row=1, column=1, padx=5, pady=1)

        self.v_apellido = tk.StringVar()
        self.entrada_apellido = tk.Entry(self, textvariable=self.v_apellido)
        self.entrada_apellido.config(width=50, font=('Arial', 12),bg='green')
        self.entrada_apellido.grid(row=2, column=1, padx=5, pady=1)

        self.v_fnacimiento = tk.StringVar()
        self.entrada_fnacimiento = tk.Entry(self, textvariable=self.v_fnacimiento)
        self.entrada_fnacimiento.config(width=50, font=('Arial', 12),bg='green')
        self.entrada_fnacimiento.grid(row=3, column=1, padx=5, pady=1)


        self.v_telefono = tk.StringVar()
        self.entrada_telefono = tk.Entry(self, textvariable=self.v_telefono)
        self.entrada_telefono.config(width=50, font=('Arial', 12),bg='green')
        self.entrada_telefono.grid(row=4, column=1, padx=5, pady=1)

        self.v_genero = tk.StringVar()
        self.entrada_genero = tk.Entry(self, textvariable=self.v_genero)
        self.entrada_genero.config(width=50, font=('Arial', 12),bg='green')
        self.entrada_genero.grid(row=5, column=1, padx=5, pady=1)
        
        self.v_direccion = tk.StringVar()
        self.entrada_direccion = tk.Entry(self, textvariable=self.v_direccion)
        self.entrada_direccion.config(width=50, font=('Arial', 12),bg='green')
        self.entrada_direccion.grid(row=6, column=1, padx=5, pady=1)

        self.v_localidad = tk.StringVar()
        self.entrada_localidad = tk.Entry(self, textvariable=self.v_localidad)
        self.entrada_localidad.config(width=50, font=('Arial', 12),bg='green')
        self.entrada_localidad.grid(row=7, column=1, padx=5, pady=1)

        self.v_email = tk.StringVar()
        self.entrada_email = tk.Entry(self, textvariable=self.v_email)
        self.entrada_email.config(width=50, font=('Arial', 12),bg='green')
        self.entrada_email.grid(row=8, column=1, padx=5, pady=1)
        #Botones

        self.boton_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.boton_nuevo.config(width=25, font=('Arial', 10), fg='White', bg='#1671aa',
                               cursor='hand2', activebackground = '#f8ce18' )
        self.boton_nuevo.grid(row=10, column=0, padx=5, pady=5)

        self.boton_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(width=25, font=('Arial', 10), fg='White', bg='#1671aa',
                               cursor='hand2', activebackground = '#f8ce18' )
        self.boton_guardar.grid(row=10, column=1, padx=5, pady=5)

        self.boton_borrar = tk.Button(self, text='Borrar', command=self.deshabilitar)
        self.boton_borrar.config(width=25, font=('Arial', 10), fg='White', bg='#1671aa',
                               cursor='hand2', activebackground = '#f8ce18' )
        self.boton_borrar.grid(row=10, column=2, padx=5, pady=5)

    def habilitar(self):
        self.entrada_nombre.config(state='normal')
        self.entrada_apellido.config(state='normal')
        self.entrada_fnacimiento.config(state='normal')
        self.entrada_telefono.config(state='normal')
        self.entrada_genero.config(state='normal')
        self.entrada_direccion.config(state='normal')
        self.entrada_localidad.config(state='normal')
        self.entrada_email.config(state='normal')
        self.boton_guardar.config(state='normal')
        self.boton_borrar.config(state='normal')

    def deshabilitar(self):
        self.v_nombre.set('')
        self.v_apellido.set('')
        self.v_fnacimiento.set('')
        self.v_telefono.set('')
        self.v_genero.set('')
        self.v_direccion.set('')
        self.v_localidad.set('')
        self.v_email.set('')
        self.entrada_nombre.config(state='disabled')
        self.entrada_apellido.config(state='disabled')
        self.entrada_fnacimiento.config(state='disabled')
        self.entrada_telefono.config(state='disabled')
        self.entrada_genero.config(state='disabled')
        self.entrada_direccion.config(state='disabled')
        self.entrada_localidad.config(state='disabled')
        self.entrada_email.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_borrar.config(state='disabled')
   
    def guardar_datos(self):
        cliente = Cliente(
            self.v_nombre.get(),
            self.v_apellido.get(),
            self.v_fnacimiento.get(),
            self.v_telefono.get(),
            self.v_genero.get(),
            self.v_direccion.get(),
            self.v_localidad.get(),
            self.v_email.get(),
            )

            
        if self.id_cli == None:
            guardar_cliente(cliente)
        else:
            modificar_cliente(self.id_cli,cliente)


        self.tabla_clientes()

        self.deshabilitar()

    def tabla_clientes(self):
        self.lista_de_clientes = mostrar_clientes()
        self.lista_de_clientes.reverse()
        self.tabla = ttk.Treeview(self,
        column = ('Nombre','Apellido','Fecha','Telefono','Genero','Direccion','Localidad','E-mail'))
        self.tabla.grid(row=11, column=0, columnspan=5, sticky='nse')
       
        # scroll bar
        self.scroll_vertical = ttk.Scrollbar(self,
        orient = 'vertical', command=self.tabla.yview)
        self.scroll_vertical.grid(row=11,column=11, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll_vertical.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Apellido')
        self.tabla.heading('#3', text='Fecha de Nacimiento')
        self.tabla.heading('#4', text='Telefono')
        self.tabla.heading('#5', text='Genero')
        self.tabla.heading('#6', text='Direccion')
        self.tabla.heading('#7', text='Localidad')
        self.tabla.heading('#8', text='E-mail')
        self.tabla["displaycolumns"]=("Nombre","Apellido","Telefono","Direccion","Localidad")
        
        



        #cargar datos desde la tabla 
        for cli in self.lista_de_clientes:
            self.tabla.insert('',0, text=cli[0],
            values = (cli[1],cli[2],cli[3],cli[5],cli[4],cli[6],cli[7],cli[8]))

        self.boton_borrar = tk.Button(self, text='Borrar', command=self.deshabilitar)
        self.boton_borrar.config(width=25, font=('Arial', 10), fg='White', bg='#1671aa',
                               cursor='hand2', activebackground = '#f8ce18' )
        self.boton_borrar.grid(row=12, column=0, padx=5, pady=5)

        self.boton_editar = tk.Button(self, text='Editar', command=self.editar_cliente)
        self.boton_editar.config(width=25, font=('Arial', 10), fg='White', bg='#1671aa',
                               cursor='hand2', activebackground = '#f8ce18' )
        self.boton_editar.grid(row=12, column=1, padx=5, pady=5)
 
    def editar_cliente(self):
        self.id_cli = self.tabla.item(self.tabla.selection())['text']
        self.nom_cli = self.tabla.item(self.tabla.selection())['values'][0]
        self.ape_cli = self.tabla.item(self.tabla.selection())['values'][1]
        self.fen_cli = self.tabla.item(self.tabla.selection())['values'][2]
        self.tel_cli = self.tabla.item(self.tabla.selection())['values'][4]
        self.gen_cli = self.tabla.item(self.tabla.selection())['values'][3]
        self.dir_cli = self.tabla.item(self.tabla.selection())['values'][5]
        self.loc_cli = self.tabla.item(self.tabla.selection())['values'][6]
        self.ema_cli = self.tabla.item(self.tabla.selection())['values'][7]


        self.habilitar()  

        self.entrada_nombre.insert(0, self.nom_cli)    
        self.entrada_apellido.insert(0, self.ape_cli)
        self.entrada_fnacimiento.insert(0, self.fen_cli)
        self.entrada_telefono.insert(0, self.tel_cli)
        self.entrada_genero.insert(0,self.gen_cli)
        self.entrada_direccion.insert(0, self.dir_cli)
        self.entrada_localidad.insert(0, self.loc_cli)
        self.entrada_email.insert(0, self.ema_cli)




        

    def escribaFecha(event):
        if event.char.isdigit():
            texto = self.entrada_fnacimiento.get()
            letras = 0
            for i in texto:
                letras +=1
                if letras == 2:
                    self.entrada_fnacimiento.insert(2,"/")
                elif letras == 5:
                    self.entrada_fnacimiento.insert(5,"/")
        else:
            return "break"









   