import sqlite3
conn = sqlite3.connect(r"D:\Narawit_Python\Week6\example.db")
c = conn.cursor()
try:
    c.execute('SELECT * FROM users ORDER BY id ')
    conn.commit()
    result = c.fetchall()
    for x in result:
        print(x)
    c.close()
except sqlite3.Error as e:
    print(e)
finally:
    if conn:
        conn.close()
