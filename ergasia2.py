import random
import math
n=input("Give term : ")
n=int(n)
k = 0
l = 1
if (n == 1) :
    print("1")
    print("Uneven number")
elif (n == 2) :
    print("1")
    print("Uneven number")
elif (n == 3):
    print("2")
    print("Uneven number")
else:

    for i in range(1,n):
        m = k + l
        k = l
        l = m
        #print(m)
if (n > 3):
    p = m
    pl = 0
    for loop in range(20):
        a = random.randrange(p)
        if ((a**p)%p == a%p):
            pl = pl + 1
    if (pl == 20):
        print(p, " Prwtos arithmos")
    else:
        print(p, " Oxi prwtos arithmos")
