'''import os
choice = 0
filename = ''

def manu():
    global choice
    print('manu\n 1.Open Discord\n 2.Open Line\n 3.Exit ')
    choice = input('select Manu')


def opennotpad():
    filename = 'C:\\Users\\User\\AppData\\Local\\Discord'
    print('Memorandum writing %s' % filename)
    os.system(filename)


def opencalculator():
    filename ='C:\\Users\\User\\AppData\\Local\\Line\\bin'
    print('Calculator Number %s' %filename)
    os.system(filename)

while True:
    manu()
    if  choice == '1':
         opencalculator()
    elif choice == '2':
        opennotpad()
    else:
        break'''
'''def introduce (arg1,arg2 = 'com',arg3 = 'ed',arg4 = 'kku'):
    print('hello, I am '+arg1+','+arg2+''+arg3+''+arg4)
introduce('python')
introduce(arg1 = 'python')
introduce(arg1 = 'python',arg3= 'sci')
introduce('python',arg4= 'cmu')'''
from os import system, name
higt = []
low = [0,0,0,0]
print('\tโปรแกรมซื้อสินค้า\n','_'*70,'\n\t1.แสดงสินค้า\n','\t2.เพิ่มสินค้า\n','\t3.ลบสินค้า\n','\t4.แสดงสินค้าที่เลือก\n','\t5.ปิดโปรแกรม\n')
def clear():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
def sine():
    print('\tแสดงรายการสินค้า\n','_'*70,'\n\t1.เสื้อ 50 บาท\n','\t2.กางเกง 100 บาท\n','\t3.รองเท้า 150 บาท\n','\t4.กระเป๋า 200 บาท\n')
def mix():
    print('\tเพิ่มรายการสินค้า\n','_'*70)
    while True:
        print('กรุณาใส่หมายเลขสินค้า','\nกด 5 เพื่อออก\n')
        a = input()
        try:
            if int(a) == 1 :
                higt.append('เสื้อ')
                low[0] +=1
            elif int(a) == 2 :
                higt.append('กางเกง')
                low[1] +=1
            elif int(a) == 3 :
                higt.append('รองเท้า')
                low[2] +=1
            elif int(a) == 4 :
                higt.append('กระเป๋า')
                low[3] +=1
            elif int(a) == 5 :
                break
            else:
                print('กรุณาใส่หมายเลขสินค้าให้ถูกต้อง')
        except:
            print('กรุณาใส่หมายเลขให้ถูกต้อง')
            pass
def tan():
    print('\tลบรายการสินค้า\n','_'*70)
    while True:
        print('กรุณาใส่หมายเลขสินค้า','\nกด 5 เพื่อออก\n')
        b = input()
        try:
            if int(b) == 1 :
                low[0] -=1
            elif int(b) == 2 :
                low[1] -=1
            elif int(b) == 3 :
                low[2] -=1
            elif int(b) == 4 :
                low[3] -=1
            elif int(b) == 5 :
                break
            else:
                print('กรุณาใส่หมายเลขสินค้าให้ถูกต้อง')
        except:
            print('กรุณาใส่หมายเลขให้ถูกต้อง')
            pass
def aec():
    monney =low[0]*50+low[1]*100+low[2]*150+low[3]*200 
    print('\tแสดงสินค้าและจำนวน\n','_'*70)
    for x in range(0,4):
        print(higt[x],'จำนวน',low[x],'ชิ้น')
    print('ราคาสินค้าทั้งหมด = ',monney,'บาท')
while True:
    x = int(input('กรุณาเลือกรายการ : '))
    if x == 1:
        sine()
    elif x == 2:
        mix()
    elif x == 3:
        tan()
    elif x == 4:
        aec()
    elif x == 5:
        print('\tปิดโปรแกรม\n','_'*70)
        break
clear()