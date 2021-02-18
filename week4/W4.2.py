from os import system, name
dictionary ={}
def menu():
    print('\n','\tพจนานุกรม\n','\t 1.เพิ่มศัพท์\n\t','2.ลบศัพท์\n\t','3.แสดงศัพท์\n\t','4.ปิดโปรแกรม\n','-'*50)
def term():
    a = input('เพิ่มคำศัพท์ : ')
    b = input('ชนิดของคำ n. , v. , adj. , adv. : ')
    c = input('ความหมาย : ')
    dictionary[a]=b,c
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')
def delet():
    delet = input('ใสศัพท์ที่จะลบ : ')
    del dictionary[delet]
    print('ลบคำศัพท์เรียบร้อยแล้ว')
def pr():
    print('\t\t       คำศัพท์\n','-'*50,'\n','\tคำศัพท์','ประเภท','\tความหมาย')
    for x in dictionary:
        print('\t',x,'\t',dictionary[x])
def clear():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
menu()
while True:
    x = int(input('กรุณาเลือกทำรายการ : '))
    if x == 1:
        term()
    elif x == 2:
        delet()
    elif x == 3:
        pr()
    elif x == 4:
        print('ปิดโปรแกรม bye')
        break
clear()