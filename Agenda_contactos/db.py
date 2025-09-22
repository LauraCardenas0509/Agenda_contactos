import sqlite3

def init_db():
    conn = sqlite3.connect("contacts.db")  # se crea contacts.db si no existe
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_contact(name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
                   (name, phone, email))
    conn.commit()
    conn.close()

def get_contacts(search_term=None):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    if search_term:
        cursor.execute(
            "SELECT id, name, phone, email FROM contacts WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?",
            (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%")
        )
    else:
        cursor.execute("SELECT id, name, phone, email FROM contacts")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_contact(contact_id, name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?",
                   (name, phone, email, contact_id))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()
