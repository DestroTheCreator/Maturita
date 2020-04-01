import re 
f = open('School/Maturita/texty/31.txt','r').read()

cisla = re.findall(r'\d+',f)
jedla = re.findall(r'[czhm]',f)
print('pocet jedal:',len(cisla))
ar = []
pocet = []
for i in range(len(jedla)):
    jed = jedla[i]
    if jed not in ar:
        ar.append(jed)
        a = jedla.count(jed)
        pocet.append(a)
        if a < 10:
            print(jed,'sa neoplati')
            for jj in range(len(jedla)):
                j = jedla[jj]
                if j == jed:
                    print(cisla[jj])
print(ar,pocet)