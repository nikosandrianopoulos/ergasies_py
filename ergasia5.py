import random
sunolo=0
n=input("Give dimension 3 or higher:")
#Με <3 δεν σχηματίζονται τριάδες
m=input("Give dimension 3 or higher:")
#Με <3 δεν σχηματίζονται κάθετες ή διαγώνιες τριάδες
for loop in range(1, 101):
    sos=0
    n=int(n)
    m=int(m)
    k=n*m
    if (k%2==1):
        l=(k//2)+1
    else:
        l=k//2
    list=[]
    for i in range(0, l):
        list.append("S");
    for i in range(l, k):
        list.append("O");
    random.shuffle(list)
    for j in range(1,m+1):
        for i in range(1, n+1):
            if (list[i]=="S" and list[i+1]=="O" and list[i+2]=="S"):
                sos += 1
            if (list[i]=="S" and list[i+m]=="O" and list[i+(2*m)]=="S"):
                sos += 1
            if (list[i]=="S" and list[i+(m+1)]=="O" and list[i+(m+2)]=="S"):
                sos += 1
    sunolo += sos
mo=(sunolo/100)
print(mo,"%")
