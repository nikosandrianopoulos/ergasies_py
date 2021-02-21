import urllib.request
import json
from datetime import date
tday=date.today()
year=tday.year
month=tday.month
if (month<10):
    #Στο api δέχεται τους μήνες με τουλάχιστον 2 ψηφία. Για παράδειγμα δεν δέχεται το 1, αλλά το 01
    month=str(month)
    month="0"+month
day=tday.day
year=str(year)
month=str(month)
#print(year,month,day)
tday=str(tday)
#print(tday)

sum=[]
for loopday in range(1,day+1):
    if (loopday<10):
        loopday=str(loopday)
        loopday="0"+loopday
    loopday=str(loopday)
    lag="https://api.opap.gr/draws/v3.0/1100/draw-date/"+year+"-"+month+"-"+loopday+"/"+year+"-"+month+"-"+loopday+"/draw-id"
    d=urllib.request.urlopen(lag)
    html2=d.read()
    html2=html2.decode()
    drawidd=json.loads(html2, strict = False)
    d=str(drawidd[0])
    numb="https://api.opap.gr/draws/v3.0/1100/draw-id/"+"/"+ d + "/" + d
    d=urllib.request.urlopen(numb)
    htmll=d.read()
    htmll=htmll.decode()
    winumb=json.loads(htmll, strict = False)
    for draw in winumb['content']:
        #print(draw['winningNumbers']['list'])
        sum = sum + draw['winningNumbers']['list']
#print(sum)
sum.sort()
stats=[]
for loop in range(80):
    stats.append(0)
k=0

for x in range(len(sum)-1):
    if(sum[x]==sum[x+1]):
        stats[k] += 1
    else:
        k += 1
        stats[k] += 1
athr=0
for x in range(80):
    #Athrisma stoixeiwn gia M.O
    athr += stats[x]
for x in range(80):
    print("O arithmos",x+1,"emfanistike",stats[x]/athr,"%")
