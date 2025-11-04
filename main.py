from encrypt import insert_user
from decrypt import show_users
import sqlite3
from prettytable import PrettyTable
import os

def clear_console():
    # Nếu là Windows thì dùng 'cls', còn lại dùng 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')


def delete_user_by_id(user_id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    print(f"🗑️ Đã xóa user có ID {user_id}")

def delete_user_by_name(name):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE name=?", (name,))
    conn.commit()
    conn.close()
    print(f"🗑️ Đã xóa user có tên {name}")

def show_raw_users():
    """Xuất dữ liệu thô trong DB (chưa giải mã)"""
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    table = PrettyTable()
    table.field_names = ["ID", "Name", "Phone (raw)", "Email (raw)", "CCCD (raw)"]

    for row in rows:
        table.add_row(row)

    print(table)

def menu():
    while True:
        clear_console()
        print("\n=== MENU ===")
        print("1. Nhập dữ liệu (mã hóa & lưu)")
        print("2. Xuất dữ liệu (giải mã & hiển thị)")
        print("3. Xóa theo ID")
        print("4. Xóa theo tên")
        print("5. Xuất dữ liệu thô (chưa giải mã)")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            name = input("Tên: ")
            phone = input("SĐT: ")
            email = input("Email: ")
            cccd = input("CCCD: ")
            insert_user(name, phone, email, cccd)
            input("\nNhấn Enter để tiếp tục...")

        elif choice == "2":
            print("\n📋 Dữ liệu đã giải mã trong DB:")
            show_users()
            input("\nNhấn Enter để tiếp tục...")

        elif choice == "3":
            user_id = int(input("Nhập ID cần xóa: "))
            delete_user_by_id(user_id)
            input("\nNhấn Enter để tiếp tục...")

        elif choice == "4":
            name = input("Nhập tên cần xóa: ")
            delete_user_by_name(name)
            input("\nNhấn Enter để tiếp tục...")

        elif choice == "5":
            print("\n📋 Dữ liệu thô trong DB (chưa giải mã):")
            show_raw_users()
            input("\nNhấn Enter để tiếp tục...")

        elif choice == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")
            input("\nNhấn Enter để tiếp tục...")


if __name__ == "__main__":
    menu()
