"""Libreria para conectar con sqlite3"""
import sqlite3

def main():
    try:
        conn = sqlite3.connect("db/db_prueba.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM clientes limit 10;")
        rows = cur.fetchall()
        print(rows)
        conn.close()
    except sqlite3.DatabaseError as e:
        print(e.args[0])

if __name__ == "__main__":
    main()
