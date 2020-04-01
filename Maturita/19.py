import re
f = open('School/Maturita/texty/19.txt','r').read()
nazvy = re.findall(r'[A-Za-z ]+',f)
print(nazvy)
nastup = re.findall(r'[^;][0-9]+',f)
vystup = re.findall(r'[;][0-9]+',f)
print(nastup,vystup)

elektri = ['long','ccagood','shortaf']

def inti(c):
    return int(c)

def subi(k):
    k = re.sub(';',' ',k)
    k = int(k)
    return k

nastup = [inti(c) for c in nastup]
print(nastup)
vystup = [subi(k) for k in vystup]
print(vystup)

a = 0

for i in range(len(nazvy)):
    a += nastup[i]-vystup[i]
    if a < 20:
        ele = elektri[2]
    elif a < 70:
        ele = elektri[1]
    else:
        ele = elektri[0]
    print(nazvy[i],a,ele)

print('---------------------------')

for j in range(len(nazvy)):
    if nastup[j] < 3 and vystup[j] < 3:
        print(nazvy[j],'na znamenie')
    else:
        print(nazvy[j],'origos')
print('-----------------------')
for k in range(len(nazvy)):
    if nastup[k] >= 10:
        print('automat na ',nazvy[k])
