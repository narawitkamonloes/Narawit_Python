"""name=input("What is your name?\n")
surname=input("What is your surname?\n")
year=input("What is your year?\n")
StudentCode=input("What is your Student code?\n")
print("\n\n")
print("%s"%name,surname)
print("%s"%year) 
print("%s"%StudentCode)"""
a=[]
while True:
    b = input("\tร้านซีเบเกอรี่\t\nเพิ่ม [a}\nแสดง [s]\nออกจากระบบ [x]")
    b = b.lower()
    if b == "a":
        c = input("ป้อนข้อมูลลูกค้า(รหัส:ชื่อ:จังหวัด)")
        a.append(c)
        print("\n*********ข้อมูลได้เข้าสู่ระบบแล้ว*********\n")
    elif b == "s":
        print("{0:-<6}{0:-<10}{0:-<10}",format(""))
        print("{0:-<8}{1:-<10}{2:10}",format("รหัส","ชื่อ","จังหวัด"))
        print("{0:-<6}{0:-<10}{0:-<10}",format(""))
        for d in a:
            e = d.split(":")
            print("{0[0]:<6}{0[1]:<10}{0[2]:<10}",format(e))
            continue
    elif b == "x":
        break
print("ทำคำสั่งถัดไป")