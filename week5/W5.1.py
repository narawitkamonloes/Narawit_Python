from os import name, system
class nisit:
    def __init__(self,name,sex,year,branch,school,province):
        self.name = name
        self.sex = sex
        self.year = year
        self.branch = branch
        self.school = school
        self.province = province
    def show(self) :
        if b == 'ชาย':
            print('สวัสดีครับผมชื่อ :','{0: <8}'.format(self.name))
        elif b == 'หญิง':
            print('สวัสดีคะฉันชื่อ :')
        print('เพศ : ','{0: <8}'.format(self.sex))
        print('ชั้นปี : ','{0: <8}'.format(self.year))
        print('สาขา : ','{0: <8}'.format(self.branch))
        print('โรงเรียนที่จบ : ','{0: <8}'.format(self.school))
        print('จังหวัด : ','{0: <8}'.format(self.province))
def clear():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')
a = str(input('ชื่อ_กลุล : '))
b = str(input('เพศ : '))
c = str(input('ชั้นปี :'))
d = str(input('สาขา : '))
e = str(input('โรงเรียนที่จบ : '))
f = str (input('จังหวัด : '))  
clear()
print('-'*15,'แนะนำตัว','-'*15) 
x = nisit(a,b,c,d,e,f)
x.show()