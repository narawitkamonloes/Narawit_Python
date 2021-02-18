"""print("\tเลือกเมนูเพื่อทำรายการ\n","############################################")
print("             กด 1 เลือกเหมาจ่าย\n","            กด 2 เลือกจ่ายเพิ่ม ")
x=int(input("เลือก 1 หรือ 2 : "))
if x == 1:
    Km=int(input("กรุณาใส่ระยะทาง : "))
    if Km > 25:
        print("ค่าบิการ = 55 บาท")
    elif Km <= 25:
        print("ค่าบริการ = 25 บาท")
elif x == 2:
    Km=int(input("กรุณาใส่ระยะทาง : "))
    if Km > 25:
        print("ค่าบิการ = ",25+55,"บาท")
    elif Km <= 25:
        print("ค่าบริการ = 25 บาท")"""

"""a=int(input("Enter number "))
i=1
sum=0
while(i<=a):
    y=int(input("Ente NUmber : "))
    i+=1
    sum=sum+y
print("ผลบวกเท่ากับ ",sum)"""

"""Food=[]
i=1
y=0
x=0
while(i>0):
    Name=str(input("รายการอาหารโปรดลำดับที่ "+str([i])))
    i+=1
    if Name == "exit":
        break
    Food.append(Name)
print("อาหารสุดโปรดของคุณมีดังนี้",end="\t ")
for x in Food:
    y+=1
    print(y,".",x,end="\t ")"""

'''a=[]
while True:
    b = input('----ร้านซีเบเกอรี่----\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]\n')
    b = b.lower()
    if b == 'a':
        c =input('ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด)')
        a.append(c)
        print('\n*******ข้อมูลได้เข้าสู่ระบบแล้ว*******\n')
    elif b == 's':
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        for d in a:
            e = d.split(":")
            print('{0[0]:<6}{0[1]:<10}({0[2]:<10})'.format(e))
            continue
    elif b == 'x':
        z=input('คุณจะออกจากระบบใช่หรือไม่ yes/no : ')
        if z == 'yes':
            print('-----ออกจากระบบแล้ว-----')
            break
print('ทำคำสั่งต่อไป')'''

print('-'*40)
s = int(input('Please Enter Students : '))
print('-'*40,'\n')
point = [0,0,0,0,0,0]
score = ['0-49:','50-59:','60-69:','70-79:','80-89:','90-100:']
i = 1
while i <= s :
    p = int(input('[%d] Please Enter Score : '%i))
    i += 1
    if p >= 0 and p<=49 :
        point[0] +=1
    elif p >= 50 and p <= 59:
        point[1] +=1
    elif p >= 60 and p <= 69:
        point[2] +=1
    elif p >= 70 and p <= 79:
        point[3] +=1
    elif p >= 80 and p <= 89:
        point[4] +=1
    elif p >= 90 and p <= 100:
        point[5] +=1
print('-'*40)
for x in  range(0,6):
    print(score[x],'*'*point[x])
    