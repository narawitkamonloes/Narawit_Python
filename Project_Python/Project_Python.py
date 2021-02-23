from os import name,system
import sqlite3
import datetime
conn = sqlite3.connect(r"D:\Narawit_Python\Project_Python\Project_Python.db")
c = conn.cursor()
#c.execute ('''CREATE TABLE users (NO integer PRIMARY KEY AUTOINCREMENT,
#    dd varchar(100) NOT NULL,
#    tt varchar(100) NOT NULL,
#    that varchar(100) NOT NULL,
#    nname varchar(100) NOT NULL,
#    size varchar(100) NOT NULL,
#    kind varchar(100) NOT NULL,
#    more varchar(100) NOT NULL,
#    price varchar(100) NOT NULL)''')
#conn.commit()
#conn.close()
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def  menu():
    global king
    print('\tเพิ่มเมนู    [a]\n','\tแสดงเมนู   [s]\n','\tแก้ไขเมนู   [e]\n','\tลบเมนู     [d]\n','\tปิดโปรแกรม [x]\n','-'*28)
    king = input('เลือกายการที่ต้องการ : ')
def add():
    global dd,tt,that,nname,size,kind,more
    T= datetime.datetime.today()
    da = datetime.date.today()
    tt= str(T.time())
    dd = str(da)
    while True:
        that = int(input('หมายเลขโต๊ะ 1-10 : '))
        if that <= 0 or that >= 11 :
            print('กรุณากรอกข้อมูลอีกครั้ง')
        else:
            break
    nname = input('ชื่อ : ')
    print('\n','******* เลือกขนาดของภาชนะ *******')
    print('s ราคา 50 บาท','\nm ราคา 80 บาท','\nl ราคา 110 บาท','\nxl ราคา 140 บาท') 
    while True:
        size = input('เลือกขนาด s m l xl : ')
        if size != 's'and size !='m'and size !='l'and size !='xl' and size != 'S'and size !='M'and size !='L'and size !='XL':
            print('กรุณากรอกข้อมูลอีกครั้ง')
        else:
            break
    print('\n','******* เลือกรสชาตที่ต้องการ *******')
    print('\n1.ผลไม้รวม  2.ลำใย  3.เงาะ  4.เมล่อน  5.ทุเรียน')
    while True:
        kind = int(input('ใส่หมายเลขชนิด : '))
        if kind == 1:
            kind = 'ผลไม้รวม'
            break
        elif kind == 2:
            kind = 'ลำใย'
            break
        elif kind == 3:
            kind = 'เงาะ'
            break
        elif kind == 4:
            kind = 'เมล่อน'
            break
        elif kind == 5:
            kind = 'ทุเรียน'
            break
        else:
            print('ใส่หมายเลขให้ถูกต้อง')
    print('\n','******* เลือกสิ่งที่จะใส่เพิ่ม *******')
    print('1.วิปครีม    20 บาท','\n2.ช็อคโกแลต 20 บาท' ,'\n3.วิป&ช็อค  30 บาท','\n4.ไม่เพิ่ม\n','1.วิปครีม 2.ช็อคโกแลต 3.วิป&ช็อค 4.ไม่เพิ่ม')
    while True:
        more = int(input('ใส่หมายเลขสิงเพิ่มเติม : '))
        if more == 1:
            more = 'วิปครีม'
            break
        elif more == 2:
            more = 'ช็อคโกแลต'
            break
        elif more == 3:
            more = 'วิป&ช็อค'
            break
        elif more == 4:
            more = '-'
            break
        else:
            print('ใส่หมายเลขให้ถูกต้อง')
def add1():
    global dd,tt,that,nname,size,kind,more
    T= datetime.datetime.today()
    da = datetime.date.today()
    tt= str(T.time())
    dd = str(da)
    nname = input('ชื่อ : ')
    print('\n','******* เลือกขนาดของภาชนะ *******')
    print('s ราคา 50 บาท','\nm ราคา 80 บาท','\nl ราคา 110 บาท','\nxl ราคา 140 บาท') 
    while True:
        size = input('เลือกขนาด s m l xl : ')
        if size != 's'and size !='m'and size !='l'and size !='xl' and size != 'S'and size !='M'and size !='L'and size !='XL':
            print('กรุณากรอกข้อมูลอีกครั้ง')
        else:
            break
    print('\n','******* เลือกรสชาตที่ต้องการ *******')
    print('\n1.ผลไม้รวม  2.ลำใย  3.เงาะ  4.เมล่อน  5.ทุเรียน')
    while True:
        kind = int(input('ใส่หมายเลขชนิด : '))
        if kind == 1:
            kind = 'ผลไม้รวม'
            break
        elif kind == 2:
            kind = 'ลำใย'
            break
        elif kind == 3:
            kind = 'เงาะ'
            break
        elif kind == 4:
            kind = 'เมล่อน'
            break
        elif kind == 5:
            kind = 'ทุเรียน'
            break
        else:
            print('ใส่หมายเลขให้ถูกต้อง')
    print('\n','******* เลือกสิ่งที่จะใส่เพิ่ม *******')
    print('1.วิปครีม    20 บาท','\n2.ช็อคโกแลต 20 บาท' ,'\n3.วิป&ช็อค  30 บาท','\n4.ไม่เพิ่ม')
    print('1.วิปครีม 2.ช็อคโกแลต 3.วิป&ช็อค 4.ไม่เพิ่ม')
    while True:
        more = int(input('ใส่หมายเลขสิงเพิ่มเติม : '))
        if more == 1:
            more = 'วิปครีม'
            break
        elif more == 2:
            more = 'ช็อคโกแลต'
            break
        elif more == 3:
            more = 'วิป&ช็อค'
            break
        elif more == 4:
            more = '-'
            break
        else:
            print('ใส่หมายเลขให้ถูกต้อง')
def mon():
    global price
    sm,sam=0,0
    try:
        if size == 's'or size =='S':
            sm = 50
        elif size == 'm'or size =='M':
            sm = 80
        elif size == 'l'or size =='L':
            sm = 110
        elif size == 'xl'or size =='XL':
            sm = 140
    except:
        print('ใส่หมายเลขให้ถูกต้อง')
    try:
        if more == 'วิปครีม':
            sam = 20
        elif more == 'ช็อคโกแลต':
            sam = 20
        elif more == 'วิป&ช็อค':
            sam = 30
        elif more == '-':
            sam = 0
    except:
        print('ใส่หมายเลขให้ถูกต้อง')
    price = sam+sm
def insert (dd,tt,that,nname,size,kind,more,price) :
    try :
        conn = sqlite3.connect (r"D:\Narawit_Python\Project_Python\Project_Python.db")
        c = conn.cursor()
        sql = '''INSERT INTO users (dd,tt,that,nname,size,kind,more,price) VALUES (?,?,?,?,?,?,?,?)'''
        data = (dd,tt,that,nname,size,kind,more,price)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close ()
def show():
    print('\n{0:<8}{1:<16}{2:<19}{3:<15}{4:<15}{5:<15}{6:<15}{7:<20}{8}\n'.format('ลำดับ','วันที่','เวลา','โต๊ะที่','ชื่อ','ขนาด','รสชาติ','สิ่งที่เพิ่ม','เป็นเงิน'))
    show1="""SELECT * FROM users """
    for  x in c.execute(show1):
        print('{0:<7}{1:<13}{2:<19}{3:<12}{4:<13}{5:<15}{6:<16}{7:<16}{8}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))
def edit():
    micky = input('ลำาดับที่ : ')
    add1()
    mon()
    conn = sqlite3.connect (r"D:\Narawit_Python\Project_Python\Project_Python.db")
    c = conn.cursor()
    update_data = (dd,tt,nname,size,kind,more,price,micky)
    c.execute ('''UPDATE users SET dd = ?,tt= ?,nname= ?,size= ?,kind= ?,more= ?,price= ? WHERE NO = ?''',update_data)
    conn.commit()
    conn.close()
def delete():
    Saitama = input('ลำดับที่ต้องการลบ : ')
    conn = sqlite3.connect(r"D:\Narawit_Python\Project_Python\Project_Python.db")
    c = conn.cursor()
    c.execute('''DELETE FROM users WHERE No = ?''',Saitama)
    conn.commit()
    conn.close()
while True:
    menu()
    if king == 'a':
        add()
        mon()
        insert (dd,tt,that,nname,size,kind,more,price)
    elif king == 's':
        show()
    elif king == 'e':
        edit()
    elif king == 'd':
        delete()
    elif king == 'x':
        print('\tออกจากดปรแกรม')
        Genos=str(input('\tต้องการออกจาระบบหรือไม่ Yes/No : '))
        if Genos == 'Yes':
            clear()
            break
    else:
        print('กรุณากรอกข้อมูลอีกครั้ง')