import os,datetime
name,score,time,hit=[],[],[],[]
def timer():
    x = datetime.datetime.now().replace(microsecond=0)
    print(x)
num = int(input('Number of participants : '))
m=1
while m <= num:
    m+=1
    n = str(input('Enter Name of participant : ') )
    s = float(input('Enter your csore : '))
    t = float(input('Enter your time : '))
    name.append(n)
    score.append(s)
    time.append(t)
    hit.append(s/t)
for x in range(num):
    y=x
    for y in range(num):
        if hit[x]>hit[y]:
            a,b,c,d = hit[x],name[x],score[x],time[x]
            hit[x],name[x],score[x],time[x] = hit[y],name[y],score[y],time[y]
            hit[y],name[y],score[y],time[y] = a,b,c,d
os.system('cls')
x = datetime.datetime.now()
print('Shotgun',x.strftime('%A'),'training',x.year)
print('condtion:1')
timer()
i=0
print('-'*97)
print('{0:-<5}{1:-<7}{2:-<15}{3:-<17}{4:-<17}{5:-<19}{6}'.format('No','PTS','TIME','HIT FACTOR','STAGE POINTS','STAGE PERCENT','COMPETITOR# Name'))
print('-'*97)
for x in range(num):
    i+=1
    point = (hit[x]/hit[0])*50
    percent = (point/(hit[0]/hit[0]*50))*100
    print('{0:<5}{1:<7}{2:<15}{3:<17}{4:<17}{5:<19}{6}'.format(i,int(score[x]),'%.4f'%time[x],'%.4f'%hit[x],'%.4f'%point,'%.2f'%percent,name[x]))