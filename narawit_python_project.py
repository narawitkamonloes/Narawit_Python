import sqlite3
from os import name,system
conn =sqlite3.connect(r"D:\Narawit_Python\narawit_python_project.db")
c = conn.cursor()
"""c.execute ('''CREATE TABLE number (NO integer PRIMARY KEY AUTOINCREMENT,
    Fame varchar(100) NOT NULL,
    Lame varchar(100) NOT NULL,
    Email varchar(100) NOT NULL,
    id varchar(100) NOT NULL)''')
conn.commit()
conn.close()"""
def clesr ():
    if name == 'nt':
        _ = system ('cls')
    else:
        _ = system ('clear')
def menu():
    global king
    print('-'*50,'\n\tInsert [a]\n','\tShow   [s]\n','\tUpdate [e]\n','\tDelete [d]\n','\tExit   [x]\n','-'*50)
    king = input(' input your option : ')
def add():
    global Fname,Lname,Email,id,data1
    data2 = []
    data1 = input('input Fname,Lname,Email,id : ')
    data2 = data1.split(" ")
    Fname = data2[0]
    Lname = data2[1]
    Email = data2[2]
    id = data2[3]
def show():
    print(Fname,Lname,Email,id)
while True:
    menu()
    if king == 'a':
        add()
    elif king =='s':
        show()
    