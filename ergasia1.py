import random
sunolo=0
n=input("Give dimension: ")
n = int(n)
if (n < 4):
    mo = 0
else:
    for loop in range(1, 101):
        tetr=0
        k=pow(n, 2)
        if (k%2==1):
            l=(k//2)+1
        else:
            l=k//2
        list=[]
        for i in range(1, l+1):
            list.append(1);
        for i in range(l+1, k+1):
            list.append(0);
        random.shuffle(list)
        for i in range(1, n+1):
            if (list[i]==1 & list[i]==list[i+1] & list[i+1]==list[i+2] & list[i+2]==list[i+3]):
                tetr += 1
            if (list[i]==1 & list[i]==list[i+n] & list[i+n]==list[i+(2*n)] & list[i+(2*n)]==list[i+(3*n)]):
                tetr += 1
            if (list[i]==1 & list[i]==list[i+(n+1)] & list[i+(n+1)]==list[i+(n+2)] & list[i+(n+2)]==list[i+(n+3)]):
                tetr += 1
        sunolo += tetr
    mo=(sunolo/100)
print(mo,"%")
