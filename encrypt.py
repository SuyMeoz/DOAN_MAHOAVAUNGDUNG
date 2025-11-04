import sqlite3
from AES import AES

# Khóa AES 16 byte
key = b'ThisIsASecretKey'
aes = AES(key)

def pad(text):
    return text.encode().ljust(16, b'\x00')[:16]

def insert_user(name, phone, email, cccd):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone BLOB,
            email BLOB,
            cccd BLOB
        )
    ''')

    enc_phone = aes.encrypt(pad(phone))
    enc_email = aes.encrypt(pad(email))
    enc_cccd = aes.encrypt(pad(cccd))

    cursor.execute("INSERT INTO users (name, phone, email, cccd) VALUES (?, ?, ?, ?)",
                   (name, enc_phone, enc_email, enc_cccd))
    conn.commit()
    conn.close()
    print("✅ Đã thêm dữ liệu (đã mã hóa) vào DB")
