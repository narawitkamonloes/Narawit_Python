import sqlite3
conn = sqlite3.connect (r"D:\Narawit_Python\Week6\example.db")
c = conn.cursor()
try :
    data = ('B','B','B'),('C','C','C'),('D','D','D')
    c.executemany('INSERT INTO users(fname,lname,email) VALUES (?,?,?)',data)
    conn.commit()
    c.close()
except sqlite3.Error as e:
    print(e)

finally :
    if conn :
        conn.close()