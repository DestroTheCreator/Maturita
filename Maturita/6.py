f = open('School/Maturita/texty/6.txt','r')
eskit = f.read()
import re
teploty = re.findall(r'[+-][0-9]+[,][0-9]+',eskit)
miesta = re.findall(r'[M][A-Za-z0-9]+',eskit)
print (teploty,miesta,'\nmerania =',len(teploty))
maxx = -9000
maxd = -1
skit = []
for pi in teploty:
    x = re.sub(r',','.',pi)
    x = float(x)
    if x > maxx:
        maxx = x
        maxd += 1
    skit.append(x)
print(maxx,' v ',miesta[maxd])
def average(arr):
    return sum(arr)/len(arr)
print(average(skit))