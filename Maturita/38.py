import re, numpy
f = open('School/Maturita/texty/38.txt','r').read()

filmy = re.findall(r'[A-z ]+[;][A-z]',f)
mena = re.findall(r'[;][A-z ]+[;]',f)
cisla = re.findall(r'[0-9]+',f)

filmy = [re.sub(';[A-z]','',i) for i in filmy]
mena = [re.sub(';','',i) for i in mena]

cisla = numpy.reshape(cisla,(16,4))

print(filmy,mena,cisla,'\n\n\n')

navstevnost = [sum(list(int(f)for f in i))for i in cisla]


for i in range(len(navstevnost)):
    print(filmy[i],navstevnost[i])

navstevnost = numpy.array(navstevnost)
filmy = numpy.array(filmy)
ind = navstevnost.argsort()
sortfilmy = list(filmy[ind])
sortnavstevnost = list(navstevnost[ind])
print('\n\n')
for i in range(len(navstevnost)):
    print(sortfilmy[i],sortnavstevnost[i])

print('\n\n')
for i in range(7):
    print(sortfilmy[-i-1],sortnavstevnost[-i-1])

print('\n')
keho_chce = input('Daj meno')
for i in range(len(mena)):
    if str(mena[i]) == str(keho_chce):
        print(filmy[i])
        a = mena.count(keho_chce)
print(a)