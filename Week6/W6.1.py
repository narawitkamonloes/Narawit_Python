import sqlite3
def insertTouser (fname,lname,email) :
    try :
        conn = sqlite3.connect (r"D:\Narawit_Python\Week6\example.db")
        c = conn.cursor()

        sql = '''INSERT INTO users (fname,lname,email) VALUES (?,?,?)'''
        data = (fname,lname,email)
        c.execute(sql,data)
        conn.commit()
        conn.close

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :

        if conn :
            conn.close ()
insertTouser('Narawit','Kamonloes','Narawit.ka@kkumail.com')
insertTouser('Diamond','Spino','Diamondspino@kkumail.com')