import tkinter as tk
from interfaces.interface import Frame, barra_menu



def main():
    root = tk.Tk()
    root.title('Gestion de Clientes')
    root.iconbitmap('img/ico.ico')
    root.resizable(1,1) # 0,0 para que no se pueda cambiar el tamaño
    barra_menu(root)
    app = Frame(root = root)
    






    app.mainloop()

if __name__ == '__main__':
    main()
