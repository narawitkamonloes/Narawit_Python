from os import system,name
from typing import ByteString
point=[0,0,0,0]
nam=['หมวก','กางเกง','เสื้อ','ฮูต']
def clear():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
def show():
    print('แสดงรายการสินค้า','\t\n1.หมวก ใบละ 50 บาท','\t\n2.กางเกง ตัวละ 100 บาท','\t\n3.เสื้อ ตัวละ 150 บาท','\t\n4.ฮูต ตัวละ 200 บาท')
def add():
    k =input('เพิ่มรายการสินค้า :')
    if k == '1':
        nam.append('หมวก')
        point.append(0)
        point[0]+=1
    elif k == '2':
        nam.append('กางเกง')
        point.append(0)
        point[1]+=1
    elif k == '3':
        nam.append('เสื้อ')
        point.append(0)
        point[2]+=1
    elif k =='4':
        nam.append('ฮูต')
        point.append(0)
        point[3]+=1
    else:
        print('กรุณาใส่หมายเลขให้ถูกต้อง')
def dellet():
    print('ใส่หมายเลขสินค้าที่จะลบ หรือ กด u เพื่อลบทั้งหมด')
    l =input('ลบรายการสินค้าที่ : ')
    if l == '1':
        point[0]-=1
    elif l == '2':
        point[1]-=1
    elif l == '3':
        point[2]-=1
    elif l == '4':
        point[3]-=1
    elif l == 'u':
        del nam[:]
        del point[:]
    else:
        print('กรุณาใส่หมายเลขให้ถูกต้อง')
def show1():
    monney1 =point[0]*50
    monney2 =point[1]*100
    monney3 =point[2]*150
    monney4 =point[3]*200
    summonney = monney1+monney2+monney3+monney4
    print('\tแสดงสินค้าและจำนวน\n','_'*70)
    for x in range(0,4):
        print(nam[x],'จำนวน',point[x],'ชิ้น')
    print('ราคาสินค้าทั้งหมด = ',summonney,'บาท')
def exit():
    while True:
        v=str(input('ปิดโปรแกรมหรือไม่ y/n :'))
        try:
            if v == 'y':
                del nam[:]
                del point[:]
                break
            elif v == 'n':
                continue
        except:
            print('กรุณาใส่หมายเลขให้ตรง')
            pass
while True:
    print('*'*20,'นราวิศว์เดลิเวอรี่','*'*20,'\t\n1.แสดงรายการสินค้า [s]','\t\n2.เพิ่มรายการ [a]','\t\n3.ลบรายการ [d]','\t\n4.แสดงสิ่งที่เลือก [h]','\t\n5.ออกจากระบบ [e]')
    m = input('Enter your Option :')
    class shop:
        def __init__(self,hun):
            self.hun=hun
            if str(self.hun) == 's':
                show()
            elif str(self.hun)== 'a':
                add()
            elif str(self.hun)== 'd':
                dellet()
            elif str(self.hun)== 'h':
                show1()
            elif str(self.hun) == 'e':
                exit()
                clear()
            else:
                print('กรุณาใส่หมายเลขให้ถูกต้อง =_= :')
    x=shop(m)