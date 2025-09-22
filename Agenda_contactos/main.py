# Punto de entrada de la aplicación
# Aquí se inicializa la ventana principal y se carga la pantalla de inicio

import tkinter as tk
from views.home import Home
from db import init_db

def main():
    init_db()

    root = tk.Tk()
    root.title("Agenda de Contactos")
    root.geometry("500x400")

    app = Home(root)
    root.mainloop()

if __name__ == "__main__":
    main()
