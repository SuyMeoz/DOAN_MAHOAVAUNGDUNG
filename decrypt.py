import sqlite3
from AES import AES
from prettytable import PrettyTable

key = b'ThisIsASecretKey'
aes = AES(key)

def unpad(text):
    return text.decode().rstrip('\x00')

def show_users():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    table = PrettyTable()
    table.field_names = ["ID", "Name", "Phone", "Email", "CCCD"]

    for row in rows:
        id, name, phone, email, cccd = row
        table.add_row([
            id,
            name,
            unpad(aes.decrypt(phone)),
            unpad(aes.decrypt(email)),
            unpad(aes.decrypt(cccd))
        ])

    print(table)
