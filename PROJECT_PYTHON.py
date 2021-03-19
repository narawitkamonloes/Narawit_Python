from tkinter import*
import sqlite3
import datetime  
from os import  system,name
conn = sqlite3.connect(r"D:\Cmon\PROJECT_PYTHON.db")
c = conn.cursor()
# # c.execute ('''CREATE TABLE users (NO integer PRIMARY KEY AUTOINCREMENT,
# #    Dday varchar(100) NOT NULL,
# #    Ttime varchar(100) NOT NULL,
# #    That varchar(100) NOT NULL,
# #    Nname varchar(100) NOT NULL,
# #    Size varchar(100) NOT NULL,
# #    Kind varchar(100) NOT NULL,
# #    More varchar(100) NOT NULL,
# #    Price varchar(100) NOT NULL)''')
# # conn.commit(),conn.close()
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
T= datetime.datetime.today()
da = datetime.date.today()
Ttime= str(T.time())
Dday = str(da)
def Monney():
    global Price
    sm,sam=0,0
    try:
        if Size == 's'or Size =='S':
            sm = 50
        elif Size == 'm'or Size =='M':
            sm = 80
        elif Size == 'l'or Size =='L':
            sm = 110
        elif Size == 'xl'or Size =='XL':
            sm = 140
        elif Size == 'xxl'or Size == 'XXL':
            sm = 170
    except:
        print('Enter the correct number')
    try:
        if More == 'Whipped Cream':
            sam = 20
        elif More == 'Chocolate':
            sam = 20
        elif More == 'Whipped Cream & Chocolate':
            sam = 30
        elif More == '-':
            sam = 0
    except:
        print('Enter the correct number')
    Price = sam+sm
def insert_Data() :
    win.destroy()
    try :
        Monney()
        conn = sqlite3.connect (r"D:\Cmon\PROJECT_PYTHON.db")
        c = conn.cursor()
        sql = '''INSERT INTO users (Dday,Ttime,That,Nname,Size,Kind,More,Price) VALUES (?,?,?,?,?,?,?,?)'''
        data = (Dday,Ttime,That,Nname,Size,Kind,More,Price)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
           conn.close ()
    min()
def Delete_db():
    cui.destroy()
    conn = sqlite3.connect(r"D:\Cmon\PROJECT_PYTHON.db")
    c = conn.cursor()
    c.execute('''DELETE FROM users WHERE No = ?''',Number)
    conn.commit()
    conn.close()
    min()
def Editsql():
    bui.destroy()
    Monney()
    conn = sqlite3.connect (r"D:\Cmon\PROJECT_PYTHON.db")
    c = conn.cursor()
    update_data = (Dday,Ttime,Nname,Size,Kind,More,Price,No)
    c.execute ('''UPDATE users SET Dday = ?,Ttime= ?,Nname= ?,Size= ?,Kind= ?,More= ?,Price= ? WHERE NO = ?''',update_data)
    conn.commit()
    conn.close()
    min()
def one():
    global win
    win = Tk()
def two():
    global aui
    aui = Tk()
def three():
    global bui
    bui = Tk()
def four():
    global cui
    cui = Tk()
def aine():
    win.destroy()
    min()
def bine():
    aui.destroy()
    min()
def cine():
    bui.destroy()
    min()
def dine():
    cui.destroy()
    min()
def a():
    global That
    That = 1
    show()
def b():
    global That
    That = 2
    show()
def c():
    global That
    That = 3
    show()
def d():
    global That
    That = 4
    show()
def e():
    global That
    That = 5
    show()
def f():
    global That
    That = 6
    show()
def g():
    global That
    That = 7
    show()
def h():
    global That
    That = 8
    show()
def i():
    global That
    That = 9
    show()
def j():
    global That
    That = 10
    show()
def a1():
    global That
    That = 1
def b1():
    global That
    That = 2
def c1():
    global That
    That = 3
def d1():
    global That
    That = 4
def e1():
    global That
    That = 5
def f11():
    global That
    That = 6
def g1():
    global That
    That = 7
def h1():
    global That
    That = 8
def i1():
    global That
    That = 9
def j1():
    global That
    That = 10
def k():
    global Size
    Size = 'S'
    show1()
def l():
    global Size
    Size = 'M'
    show1()
def m():
    global Size
    Size = 'L'
    show1()
def n():
    global Size
    Size = 'XL'
    show1()
def o():
    global Size
    Size = 'XXL'
    show1()
def p():
    global Kind
    Kind = 'Mixed fruit'
    show2()
def q():
    global Kind
    Kind = 'Longan'
    show2()
def r():
    global Kind
    Kind = 'Rambutan'
    show2()
def s():
    global Kind
    Kind = 'Melon'
    show2()
def t():
    global Kind
    Kind = 'Durian'
    show2()
def u():
    global More
    More = 'Whipped cream'
    show3()
def v():
    global More
    More = 'Chocolate'
    show3()
def w():
    global More
    More = 'Whipped Cream & Chocolate'
    show3()
def x():
    global More
    More = ' ----- '
    show3()
def k1():
    global Size
    Size = 'S'
def l1():
    global Size
    Size = 'M'
def m1():
    global Size
    Size = 'L'
def n1():
    global Size
    Size = 'XL'
def o1():
    global Size
    Size = 'XXL'
def p1():
    global Kind
    Kind = 'Mixed fruit'
def q1():
    global Kind
    Kind = 'Longan'
def r1():
    global Kind
    Kind = 'Rambutan'
def s1():
    global Kind
    Kind = 'Melon'
def t1():
    global Kind
    Kind = 'Durian'
def u1():
    global More
def v1():
    global More
    More = 'Chocolate'
def w1():
    global More
    More = 'Whipped Cream & Chocolate'
def x1():
    global More
    More = ' ----- '
def show():
    SD.set(f'Table   =>   {That}')
def show1():
    SD1.set(f'Size     =>   {Size}')
def show2():
    SD2.set(f'Kind     =>   {Kind}')
def show3():
    SD3.set(f'More     =>   {More}')
def show5():
    SD5.set(f'Price   =>   {Price}')
def show4():
    SD4.set(f'Name   =>   {Nname}')
    show5()

def Add_data():
    global text_mas,SD,SD1,SD2,SD3,SD4,SD5
    gui.destroy()
    one()
    win.option_add('*Font','Thaisaraban 12')
    win.title('PROJECT_PYTHON')
    SD = StringVar()
    SD1 = StringVar()
    SD2 = StringVar()
    SD3 = StringVar()
    SD4 = StringVar()
    SD5 = StringVar()
    photo02=PhotoImage(file="max.png")
    Label(win,height=2,bg='firebrick2').pack(fill=X)
    Label(win,bg='deep sky blue',height=120).pack(fill=X)
    Label(win,image=photo02).place(relx=0.185 ,rely=0.06,anchor='n')
    Button(win,text='Summit',bd=5,bg='gold2',command=insert_Data).place(relx=0.13,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(win,text='back',bd=5,bg='blue2',command=aine).place(relx=0.234,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')
    Label(win,text='กรูณาเลือกหมายเลขโต๊ะของท่าน',bg= 'seagreen2').place(relx=0.59,rely=0.09,relwidth= 0.18,relheight=0.05,anchor='n')
    Label(win,text='กรูณาเลือกเลือกขนาด',bg= 'seagreen2').place(relx=0.59,rely=0.215,relwidth= 0.18,relheight=0.05,anchor='n')
    Button(win,text='1',bd=5,bg='red3',command = a).place(relx=0.39,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='2',bd=5,bg='red3',command = b).place(relx=0.44,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='3',bd=5,bg='red3',command = c).place(relx=0.49,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='4',bd=5,bg='red3',command = d).place(relx=0.54,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='5',bd=5,bg='red3',command = e).place(relx=0.59,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='6',bd=5,bg='red3',command = f).place(relx=0.64,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='7',bd=5,bg='red3',command = g).place(relx=0.69,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='8',bd=5,bg='red3',command = h).place(relx=0.74,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='9',bd=5,bg='red3',command = i).place(relx=0.79,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='10',bd=5,bg='red3',command = j).place(relx=0.84,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='S',bd=5,bg='gold2',command =k).place(relx=0.39,rely=0.28,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='M',bd=5,bg='gold2',command =l).place(relx=0.44,rely=0.28,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='L',bd=5,bg='gold2',command =m).place(relx=0.49,rely=0.28,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='XL',bd=5,bg='gold2',command =n).place(relx=0.54,rely=0.28,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(win,text='XXL',bd=5,bg='gold2',command =o).place(relx=0.59,rely=0.28,relwidth= 0.04,relheight=0.05,anchor='n')
    Label(win,text='กรูณาเลือกรสชาติที่ต้องการ',bg= 'seagreen2').place(relx=0.59,rely=0.345,relwidth= 0.18,relheight=0.05,anchor='n')
    Button(win,text='Mixed fruit',bd=5,bg='khaki',command =p).place(relx=0.41,rely=0.41,relwidth= 0.08,relheight=0.05,anchor='n')
    Button(win,text='Longan',bd=5,bg='goldenrod2',command =q).place(relx=0.50,rely=0.41,relwidth= 0.08,relheight=0.05,anchor='n')
    Button(win,text='Rambutan',bd=5,bg='red2',command =r).place(relx=0.59,rely=0.41,relwidth= 0.08,relheight=0.05,anchor='n')
    Button(win,text='Melon',bd=5,bg='sienna1',command =s).place(relx=0.68,rely=0.41,relwidth= 0.08,relheight=0.05,anchor='n')
    Button(win,text='Durian',bd=5,bg='yellow2',command =t).place(relx=0.77,rely=0.41,relwidth= 0.08,relheight=0.05,anchor='n')
    Label(win,text='กรุณาเลือกสิ่งที่ต้องการเพิ่ม',bg= 'seagreen2').place(relx=0.59,rely=0.48,relwidth= 0.18,relheight=0.05,anchor='n')
    Button(win,text='Whipped Cream',bd=5,bg='goldenrod2',command =u).place(relx=0.42,rely=0.55,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(win,text='Chocolate',bd=5,bg='red2',command =v).place(relx=0.53,rely=0.55,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(win,text='Whipped Cream & Chocolate',bd=5,bg='sienna1',command =w).place(relx=0.695,rely=0.55,relwidth= 0.21,relheight=0.05,anchor='n')
    Button(win,text='Not add',bd=5,bg='yellow2',command =x).place(relx=0.86,rely=0.55,relwidth= 0.1,relheight=0.05,anchor='n')
    Label(win,text='กรูณาใส่ชื่อของท่าน',bg= 'seagreen2').place(relx=0.430,rely=0.62,relwidth= 0.12,relheight=0.05,anchor='n')
    text_mas=Entry(win)
    text_mas.place(relx=0.56,rely=0.62,relwidth= 0.12,relheight=0.05,anchor='n')
    Button(win,text='Get',bd=5,bg='yellow2',command = text01).place(relx=0.65,rely=0.62,relwidth= 0.03,relheight=0.05,anchor='n')
    Label(win,text='S  => Price 50  Baht   /   M  => Price 80  Baht\nL  => Price 110 Baht   /   XL => Price 140 Baht \nXXL => Price 140 Baht\nWhipped cream Price 20 Baht\nChocolate Price 20 Baht\nWhipped Cream & Chocolate  Price 30 Baht').place(relx=0.62,rely=0.70,relwidth= 0.5,relheight=0.27,anchor='n')
    f1 = Frame(win,bg='cornsilk')
    f1.place(relx=0.185,rely=0.14,relwidth= 0.27,relheight=0.22,anchor='n')
    Label(f1,textvariable=SD,bg='cornsilk').place(rely=0.15,relwidth= 0.99,relheight=0.12)
    Label(f1,textvariable=SD1,bg='cornsilk').place(rely=0.25,relwidth= 0.99,relheight=0.12)
    Label(f1,textvariable=SD2,bg='cornsilk').place(rely=0.35,relwidth= 0.99,relheight=0.12)
    Label(f1,textvariable=SD3,bg='cornsilk').place(rely=0.45,relwidth= 0.99,relheight=0.12)
    Label(f1,textvariable=SD4,bg='cornsilk').place(rely=0.55,relwidth= 0.99,relheight=0.12)
    Label(f1,textvariable=SD5,bg='cornsilk').place(rely=0.65,relwidth= 0.99,relheight=0.12)
    win.attributes("-fullscreen",True)
    win.mainloop()

def Edit_data():
    global text_m,text_mm
    three()
    gui.destroy()
    bui.title('Edit')
    bui.option_add('*Font','Thaisaraban 12')
    Label(bui,height=2,bg='firebrick2').pack(fill=X)
    Label(bui,bg='deep sky blue',height=120).pack(fill=X)
    Button(bui,text='Summit',bd=5,bg='gold2',command=Editsql).place(relx=0.13,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(bui,text='back',bd=5,bg='blue2',command=cine).place(relx=0.234,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')
    Label(bui,text='กรุณาเลือกหมายเลขโต๊ะของท่าน',bg= 'seagreen2').place(relx=0.59,rely=0.09,relwidth= 0.18,relheight=0.05,anchor='n')
    Label(bui,text='กรุณาเลือกเลือกขนาด',bg= 'seagreen2').place(relx=0.59,rely=0.215,relwidth= 0.18,relheight=0.05,anchor='n')
    Button(bui,text='1',bd=5,bg='red3',command = a1).place(relx=0.39,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='2',bd=5,bg='red3',command = b1).place(relx=0.44,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='3',bd=5,bg='red3',command = c1).place(relx=0.49,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='4',bd=5,bg='red3',command = d1).place(relx=0.54,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='5',bd=5,bg='red3',command = e1).place(relx=0.59,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='6',bd=5,bg='red3',command = f11).place(relx=0.64,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='7',bd=5,bg='red3',command = g1).place(relx=0.69,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='8',bd=5,bg='red3',command = h1).place(relx=0.74,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='9',bd=5,bg='red3',command = i1).place(relx=0.79,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='10',bd=5,bg='red3',command = j1).place(relx=0.84,rely=0.154,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='S',bd=5,bg='gold2',command =k1).place(relx=0.39,rely=0.28,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='M',bd=5,bg='gold2',command =l1).place(relx=0.44,rely=0.28,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='L',bd=5,bg='gold2',command =m1).place(relx=0.49,rely=0.28,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='XL',bd=5,bg='gold2',command =n1).place(relx=0.54,rely=0.28,relwidth= 0.04,relheight=0.05,anchor='n')
    Button(bui,text='XXL',bd=5,bg='gold2',command =o1).place(relx=0.59,rely=0.28,relwidth= 0.04,relheight=0.05,anchor='n')
    Label(bui,text='กรุณาเลือกรสชาติที่ต้องการ',bg= 'seagreen2').place(relx=0.59,rely=0.345,relwidth= 0.18,relheight=0.05,anchor='n')
    Button(bui,text='Mixed fruit',bd=5,bg='khaki',command =p1).place(relx=0.41,rely=0.41,relwidth= 0.08,relheight=0.05,anchor='n')
    Button(bui,text='Longan',bd=5,bg='goldenrod2',command =q1).place(relx=0.50,rely=0.41,relwidth= 0.08,relheight=0.05,anchor='n')
    Button(bui,text='Rambutan',bd=5,bg='red2',command =r1).place(relx=0.59,rely=0.41,relwidth= 0.08,relheight=0.05,anchor='n')
    Button(bui,text='Melon',bd=5,bg='sienna1',command =s1).place(relx=0.68,rely=0.41,relwidth= 0.08,relheight=0.05,anchor='n')
    Button(bui,text='Durian',bd=5,bg='yellow2',command =t1).place(relx=0.77,rely=0.41,relwidth= 0.08,relheight=0.05,anchor='n')
    Label(bui,text='กรุณาเลือกสิ่งที่ต้องการเพิ่ม',bg= 'seagreen2').place(relx=0.59,rely=0.48,relwidth= 0.18,relheight=0.05,anchor='n')
    Button(bui,text='Whipped Cream',bd=5,bg='goldenrod2',command =u1).place(relx=0.42,rely=0.55,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(bui,text='Chocolate',bd=5,bg='red2',command =v1).place(relx=0.53,rely=0.55,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(bui,text='Whipped Cream & Chocolate',bd=5,bg='sienna1',command =w1).place(relx=0.695,rely=0.55,relwidth= 0.21,relheight=0.05,anchor='n')
    Button(bui,text='Not add',bd=5,bg='yellow2',command =x1).place(relx=0.86,rely=0.55,relwidth= 0.1,relheight=0.05,anchor='n')
    Label(bui,text='กรุณาใส่ชื่อของท่าน',bg= 'seagreen2').place(relx=0.430,rely=0.62,relwidth= 0.12,relheight=0.05,anchor='n')
    text_mm = Entry(bui)
    text_mm.place(relx=0.075,rely=0.26,relwidth= 0.06,relheight=0.05,anchor='n')
    Button(bui,text='Get',bd=5,bg='yellow2',command = NO1).place(relx=0.152,rely=0.26,relwidth= 0.03,relheight=0.05,anchor='n')
    text_m=Entry(bui)
    text_m.place(relx=0.56,rely=0.62,relwidth= 0.12,relheight=0.05,anchor='n')
    Button(bui,text='Get',bd=5,bg='yellow2',command = text02).place(relx=0.65,rely=0.62,relwidth= 0.03,relheight=0.05,anchor='n')
    Label(bui,text='กรุณาใส่ลำดับที่ต้องการแก้ไข',bg= 'seagreen2').place(relx=0.104,rely=0.19,relwidth= 0.12,relheight=0.05,anchor='n')
    Label(bui,text='S  => Price 50  Baht   /   M  => Price 80  Baht\nL  => Price 110 Baht   /   XL => Price 140 Baht \nXXL => Price 140 Baht\nWhipped cream Price 20 Baht\nChocolate Price 20 Baht\nWhipped Cream & Chocolate  Price 30 Baht').place(relx=0.62,rely=0.70,relwidth= 0.5,relheight=0.27,anchor='n')
    bui.attributes("-fullscreen",True)
    bui.mainloop()
    
def NO1():
    global No
    No = int(text_mm.get())

def text01():
    global Nname
    Nname = str(text_mas.get())
    show4()

def text02():
    global Nname
    Nname = str(text_m.get())

def Show_data():
    global man5
    two()
    jk= "--------"
    gui.destroy()
    aui.title('Edit')
    aui.option_add('*Font','Thaisaraban 12')
    f1 = Frame(aui,bg='cornsilk')
    f1.place(relx=0.5,rely=0.12,relwidth= 0.87,relheight=0.72,anchor='n')
    
    try:
        conn = sqlite3.connect(r"D:\Cmon\PROJECT_PYTHON.db")
        c = conn.cursor()
        c.execute('''SELECT * FROM users''')
        conn.commit()
        result = c.fetchall()
        for x in result:
            Label(f1,text = (x[0],jk,x[1],jk,x[2],jk,x[3],jk,x[4],jk,x[5],jk,x[6],jk,x[7],jk,x[8]),bg = "deep sky blue",height = 2).pack(fill=X,anchor='n')
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    Button(aui,text='back',bd=5,bg='blue2',command=bine).place(relx=0.234,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n') 
    aui.attributes("-fullscreen",True)
    aui.mainloop()

def nom06():
    global Number
    Number = str(miiin.get())

def Deleat_data():
    global miiin
    four()
    gui.destroy()
    cui.option_add('*Font','Thaisaraban 12')
    cui.title('PROJECT_PYTHON')
    Label(cui,bg='deep sky blue',height=120).pack(fill=X)
    Label(cui,height=2,bg='firebrick2').pack(fill=X)
    miiin = Entry(cui)
    miiin.place(relx=0.455,rely=0.26,relwidth= 0.09,relheight=0.05,anchor='n')
    Label(cui,height=2,bg='firebrick2').pack(fill=X)
    Label(cui,text='กรุณาใส่ลำดับที่ต้องการแก้ไข',bg= 'seagreen2').place(relx=0.5,rely=0.19,relwidth= 0.18,relheight=0.05,anchor='n')
    Button(cui,text='back',bd=5,bg='blue2',command=dine).place(relx=0.234,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(cui,text='Summit',bd=5,bg='gold2',command=Delete_db).place(relx=0.13,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')    
    Button(cui,text='Get',bd=5,bg='yellow2',command= nom06).place(relx=0.52,rely=0.26,relwidth= 0.03,relheight=0.05,anchor='n')
    cui.attributes("-fullscreen",True)
    cui.mainloop()

def min():
    global gui
    gui = Tk()
    gui.option_add('*Font','Thaisaraban 12')
    gui.title('PROJECT_PYTHON')
    gui.minsize(width= 1535,height=830)
    Label(gui,height=2,bg='firebrick2').pack(fill=X)
    photo01 = PhotoImage(file = "ปก02.png")
    Label(gui,image = photo01,bg='hotpink1').pack(fill=X)
    Label(gui,text=' ',bg='hotpink1',width= 20,height=5).pack(fill=X)
    Button(gui,text='Add',bd=5,bg='maroon4',command=Add_data).place(relx=0.13,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(gui,text='Show',bd=5,bg='blue2',command=Show_data).place(relx=0.234,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(gui,text='Edit',bd=5,bg='green3',command=Edit_data).place(relx=0.338,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(gui,text='Deleat',bd=5,bg='gold2',command=Deleat_data).place(relx=0.442,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')
    Button(gui,text='Exit',bd=5,bg='orange red',command= gui.destroy).place(relx=0.546,rely=0.9,relwidth= 0.1,relheight=0.05,anchor='n')
    gui.attributes("-fullscreen",True)
    gui.mainloop()
min()
clear()     