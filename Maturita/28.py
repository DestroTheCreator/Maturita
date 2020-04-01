f = open('School/Maturita/texty/28.txt','r').read()
import re,math
cisla = re.findall(r'\d+',f)
xka = []
yka = []
for i in range(len(cisla)):
    if i % 2 == 0:
        xka.append(cisla[i])
    else:
        yka.append(cisla[i])

xka = [int(i)for i in xka]
yka = [int(i)for i in yka]

print(xka,yka)

celkova = 0
vela = 0
for i in range(len(xka)-1):
    a = math.sqrt(((xka[i]-xka[i+1])**2)+((yka[i]-yka[i+1])**2))
    celkova += a
    if a > vela:
        vela = a
        den = i+1
print(celkova,'v den cislo:',den)






