import sqlite3
conn = sqlite3.connect(r"D:\Narawit_Python\Week6\example.db")
c = conn.cursor()
#c.execute ('''CREATE TABLE users (id integer PRIMARY KEY AUTOINCREMENT,
    #fname varchar(30) NOT NULL,
    #lName varchar(30) NOT NULL,
    #email varchar(100) NOT NULL)''')
c.execute('''INSERT INTO users(id,fname,lname,email) VALUES (NULL,"A","A","A")''')
c.execute('''INSERT INTO users VALUES (NULL,"B","B","B")''')
conn.commit()
conn.close()