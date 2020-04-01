import re
f = open('School/Maturita/texty/26.txt','r').read()
mena = re.findall(r'[A-Z][a-z]+',f)
krajiny = re.findall(r'[A-Z][A-Z][A-Z]',f)
skoky = re.findall(r'[0-9]+',f)
skoky = [int(i)for i in skoky]
print(list(dict.fromkeys(krajiny)))
hel = []
for i in krajiny:
    if i not in hel:
        print(i,krajiny.count(i))
    hel.append(i)

m = max(skoky)
print(skoky,m)
for i in range(len(skoky)):
    if skoky[i] == m:
        print(mena[i//5])