"""
home.py
-------
Vista principal (pantalla de inicio) de la Agenda de Contactos.
Desde aquí el usuario puede:
 - Agregar un nuevo contacto
 - Ver la lista de contactos
 - Salir de la aplicación
"""
import tkinter as tk
from views.add_contact import AddContact
from views.list_contacts import ListContacts
import styles

# Clase principal de la pantalla de inicio
class Home:
    def __init__(self, master):
        # Frame principal con el color de fondo definido en styles
        self.master = master
        self.frame = tk.Frame(master, bg=styles.BG_COLOR)
        self.frame.pack(fill="both", expand=True)

        # Título principal de la aplicación
        tk.Label(
            self.frame,
            text="📒 Agenda de Contactos",
            font=styles.TITLE_FONT,
            bg=styles.BG_COLOR,
            fg=styles.FG_COLOR
        ).pack(pady=20)

        # Botón Agregar contacto
        tk.Button(
            self.frame,
            text="➕ Agregar contacto",
            command=self.open_add_contact,
            bg=styles.BUTTON_BG,
            fg=styles.BUTTON_FG,
            font=styles.BUTTON_FONT
        ).pack(pady=10)

         # Botón para abrir la lista de contactos
        tk.Button(
            self.frame,
            text="📋 Ver contactos",
            command=self.open_list_contacts,
            bg=styles.BUTTON_BG,
            fg=styles.BUTTON_FG,
            font=styles.BUTTON_FONT
        ).pack(pady=10)

        # Botón para cerrar la aplicación
        tk.Button(
            self.frame,
            text="❌ Salir",
            command=master.quit,
            bg=styles.BUTTON_BG,
            fg=styles.BUTTON_FG,
            font=styles.BUTTON_FONT
        ).pack(pady=10)

  # Función que abre la vista de agregar contacto
    def open_add_contact(self):
        self.frame.destroy()
        AddContact(self.master, self.show_home)

  # Función que abre la vista de lista de contactos
    def open_list_contacts(self):
        self.frame.destroy()
        ListContacts(self.master, self.show_home)

  # Función que recarga la pantalla de inicio
    def show_home(self):
        self.frame.destroy()
        Home(self.master)
