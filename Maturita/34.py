import re
f = open('School/Maturita/texty/34.txt','r').read()

nazvy = re.findall(r'[A-z ]+',f)
datumy = re.findall(r'[\d ]+',f)

nazvy = [(i)for i in nazvy if i != ' ']
datumy = [(i)for i in datumy if i != ' ']
datnew = []
mx = 0
c = 0
maximalka = []
print(nazvy,datumy)
for i in datumy:
    if mx <= len(i):
        mx = len(i)
        maximalka.append(c) 
    if len(i)%2 == 0:
        i = i[:-5]
    datnew.append(i)
    c += 1
print(maximalka,datnew)
