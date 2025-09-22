# Vista para agregar un nuevo contacto
# Aquí se definen los campos de entrada y el guardado de la información
import tkinter as tk
from db import add_contact
import styles  # 👈 usamos el archivo de estilos

class AddContact:
    def __init__(self, master, back_callback):
        self.master = master
        self.back_callback = back_callback

        # Frame principal con fondo blanco
        self.frame = tk.Frame(master, bg=styles.BG_COLOR)
        self.frame.pack(fill="both", expand=True)

        # Título
        tk.Label(
            self.frame,
            text="➕ Agregar Contacto",
            font=styles.TITLE_FONT,
            bg=styles.BG_COLOR
        ).pack(pady=10)

        # Nombre
        tk.Label(self.frame, text="Nombre:", bg=styles.BG_COLOR).pack()
        self.entry_name = tk.Entry(self.frame, font=styles.INPUT_FONT)
        self.entry_name.pack(pady=5)

        # Teléfono
        tk.Label(self.frame, text="Teléfono:", bg=styles.BG_COLOR).pack()
        self.entry_phone = tk.Entry(self.frame, font=styles.INPUT_FONT)
        self.entry_phone.pack(pady=5)

        # Correo
        tk.Label(self.frame, text="Correo (opcional):", bg=styles.BG_COLOR).pack()
        self.entry_email = tk.Entry(self.frame, font=styles.INPUT_FONT)
        self.entry_email.pack(pady=5)

        # Botones
        tk.Button(
            self.frame, text="💾 Guardar",
            command=self.save_contact,
            **styles.BUTTON_STYLE
        ).pack(pady=10)

        tk.Button(
            self.frame, text="↩️ Volver",
            command=self.back_home,
            **styles.BUTTON_STYLE
        ).pack()

        # Mensajes
        self.message_label = tk.Label(self.frame, text="", fg="green", bg=styles.BG_COLOR)
        self.message_label.pack(pady=5)

    def save_contact(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        email = self.entry_email.get().strip()

        if name == "" or phone == "":
            self.message_label.config(text="⚠️ Nombre y teléfono son obligatorios", fg="red")
        else:
            add_contact(name, phone, email)
            self.message_label.config(text=f"Contacto {name} guardado ✅", fg="green")
            self.entry_name.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)

    def back_home(self):
        self.frame.destroy()
        self.back_callback()
