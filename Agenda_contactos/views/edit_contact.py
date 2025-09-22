import tkinter as tk
from tkinter import messagebox
from db import update_contact

class EditContact:
    def __init__(self, master, contact, refresh_callback):
        self.contact = contact  # contacto = (id, name, phone, email)
        self.refresh_callback = refresh_callback

        self.window = tk.Toplevel(master)
        self.window.title("✏️ Editar Contacto")

        tk.Label(self.window, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.window, width=30)
        self.entry_name.insert(0, contact[1])
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.window, text="Teléfono:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_phone = tk.Entry(self.window, width=30)
        self.entry_phone.insert(0, contact[2])
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.window, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(self.window, width=30)
        self.entry_email.insert(0, contact[3] if contact[3] else "")
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.window, text="💾 Guardar cambios", command=self.save).grid(row=3, column=0, columnspan=2, pady=10)

    def save(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        email = self.entry_email.get().strip()

        if name and phone:
            update_contact(self.contact[0], name, phone, email)
            messagebox.showinfo("Éxito", "Contacto actualizado correctamente ✅")
            self.refresh_callback()
            self.window.destroy()
        else:
            messagebox.showwarning("Error", "El nombre y teléfono son obligatorios")
