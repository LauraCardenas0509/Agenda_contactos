#  Vista para mostrar los contactos almacenados
# Se encarga de leer y mostrar los datos en pantalla
import tkinter as tk
from tkinter import messagebox
from db import get_contacts, delete_contact
from views.edit_contact import EditContact
import styles


class ListContacts:
    def __init__(self, master, back_callback):
        self.master = master
        self.back_callback = back_callback

        self.frame = tk.Frame(master, bg=styles.BG_COLOR)
        self.frame.pack(fill="both", expand=True)

        # Título
        tk.Label(
            self.frame,
            text="📒 Lista de Contactos",
            font=styles.TITLE_FONT,   # ✅ corregido
            bg=styles.BG_COLOR,
            fg=styles.FG_COLOR
        ).pack(pady=10)

        # Barra de búsqueda
        self.search_entry = tk.Entry(self.frame, width=30, font=styles.INPUT_FONT)
        self.search_entry.pack(pady=5)

        tk.Button(
            self.frame,
            text="🔍 Buscar",
            command=self.search_contacts,
            **styles.BUTTON_STYLE     # ✅ estilo unificado
        ).pack(pady=5)

        # Lista de contactos
        self.listbox = tk.Listbox(self.frame, width=50, height=10, font=styles.INPUT_FONT)
        self.listbox.pack(pady=5)

        # Botones de acciones
        btn_frame = tk.Frame(self.frame, bg=styles.BG_COLOR)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="✏️ Editar",
            command=self.edit_contact,
            **styles.BUTTON_STYLE
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="🗑️ Eliminar",
            command=self.delete_selected,
            **styles.BUTTON_STYLE
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            btn_frame,
            text="↩️ Volver",
            command=self.back_home,
            **styles.BUTTON_STYLE
        ).grid(row=0, column=2, padx=5)

        # Cargar todos los contactos al inicio
        self.load_contacts()

    def load_contacts(self, search_term=None):
        self.listbox.delete(0, tk.END)
        contacts = get_contacts(search_term)
        self.contacts_data = contacts  # guardamos datos completos

        if contacts:
            for c in contacts:
                self.listbox.insert(tk.END, f"{c[1]} | {c[2]} | {c[3] if c[3] else 'Sin correo'}")
        else:
            self.listbox.insert(tk.END, "⚠️ No hay contactos encontrados")

    def search_contacts(self):
        search_term = self.search_entry.get().strip()
        self.load_contacts(search_term)

    def edit_contact(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Error", "Seleccione un contacto primero")
            return
        index = selection[0]
        contact = self.contacts_data[index]
        EditContact(self.master, contact, self.load_contacts)

    def delete_selected(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Error", "Seleccione un contacto primero")
            return
        index = selection[0]
        contact = self.contacts_data[index]

        confirm = messagebox.askyesno("Confirmar", f"¿Eliminar a {contact[1]}?")
        if confirm:
            delete_contact(contact[0])
            self.load_contacts()

    def back_home(self):
        self.frame.destroy()
        self.back_callback()
