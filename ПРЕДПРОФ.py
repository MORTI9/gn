"""fin=open("students.csv","r", encoding="utf-8")
title=fin.readline()
students=[x.strip().split(",") for x in fin]
fin.close()
bal_sum= {}# bal_sum{key- номер класса,value-сумма оценок}
bal_cnt= {}# bal_cnt{key- номер класса,value-сумма оценок}
for x in students:
    # x[0]= порядковый номер
    # x[1] FIO
    # x[2] id
    # x[3] класс
    # x[4] оценка
    if x[4]!="None":
        if x[3] in bal_sum:
            bal_sum[x[3]]+=int(x[4])
            bal_cnt[x[3]] += 1
        else:
            bal_sum[x[3]]=int(x[4])
            bal_cnt[x[3]]=1
    fio=x[1].split()
    if fio[0]=="Хадаров" and fio[1]=="Владимир":
        print(f"Ты получил:{x[4]},за проект-{x[2]}")

for x in students:
    if x[4]=="None":
        x[4]=f'{bal_sum[x[3]] / bal_cnt[x[3]]:.3f}'
fout=open("students_new.csv","w",encoding="utf-8")
fout.write(title)
for x in students:
    fout.write(",".join(x)+"\n")
fout.close()"""
"""fin=open("students.csv","r",encoding="utf-8")
title=fin.readline()
students=[x.strip().split(",")for x in fin]
for i in range(1,len(students)):
    for j in range(i,0,-1):
        if students[j][4]<students[j-1][4]:
            students[j],students[j-1]= students[j-1],students[j]
        else:
            break

cnt=0
print("10 klass")
for x in students:
    if "10" in x[3] and x[4]=="5":
        cnt+=1
        fio = x[1].split()
        print(f"{cnt} место : {fio[1][0]}.{fio[0]}")
        if cnt==3:
            break
"""
"""fin = open("students.csv","r",encoding="utf-8")
title=fin.readline()
students=[x.strip().split(",") for x in fin]
fin.close()
while True:
    n=input("Enter number or STOP ")
    if n.upper()=="STOP":
        break
    for x in students:
        if x[2]==n:
            fio=x[1].split()
            print(f"проект номер {x[2]} делал {fio[1][0]}.{fio[0]} и получил {x[4]}")
            break
    else:
        print("Ничего не найдено")"""
"""from random import choice
fin=open("students.csv","r",encoding="utf-8")
title=fin.readline().strip()
students=[x.strip() for x in fin]
fin.close()
simbol="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
for i in range(len(students)):
    x = students[i].split(",")
    fio=x[1].split()
    login = fio[0]+"_"+fio[1][0]+fio[2][0]
    password=""
    for _ in range(8):
        password+=choice(simbol)
    students[i]=students[i]+","+login+","+password
f=open("students_password.csv","w",encoding="utf-8")
f.write(title+",Login, Password"+"\n")
for i in students:
    f.write(i+"\n")
print(f)
"""
def hash_str(st):
    p=67
    m=10**9+9
    alf="йцукенгшщзхъфывапролджэячсмитьбюё ЙЦУКЕНГЫШЩЗХФЁВАПРОЛДЖЭЯЧСМИТБЮ"
    d={}
    for ind,simbol in enumerate(alf,1):
        d[simbol]=ind
    hash_name=0
    for i in range(len(st)):
        hash_name+=d[st[i]]*p**i
    return str(hash_name%m)
fin=open("students.csv","r",encoding="utf-8")
title=fin.readline()
students=[x.strip().split(",") for x in fin]
fin.close()
fout=open("students_with_hash.csv","w",encoding="utf-8")
fout.write(title)
for x in students:
    # x[0]= id
    # x[1] FIO
    # x[2] номер проекта
    # x[3] класс
    # x[4] оценка
    s=",".join((hash_str(x[1]),x[1],x[2],x[3],x[4]))+"\n"
    fout.write(s)
fout.close()

