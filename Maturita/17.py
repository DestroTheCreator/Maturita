stringeros = ('Cez vikend je planovana odstavka severnej casti linky')
import re
slova = re.findall(r'[A-Za-z]+',stringeros)
cnt = 0
for i in slova:
    if cnt%2 == 0:
        print(i.upper())
    else:
        print(i.lower())
    cnt += 1

print('-----------------------------')
#user_input = input('zadaj volaco: ')
user_input = 'nah homie u dead mate'
newre = re.findall(r'[A-Za-z]+',user_input)
print('pocet slov je =',len(newre))
cnter = 0
for i in newre:
    if cnter%2 == 0:
        print(i.upper())
    else:
        print(i.lower())
    cnter += 1
print('-----------------------------')
laststring = 'CEZvikendJEplanovanaODSTAVKAsevernejCASTIlinky'

lastre1 = re.findall(r'[A-Z]+',laststring)
lastre2 = re.findall(r'[a-z]+',laststring)
lengt = (int(len(lastre2)))+(int(len(lastre2)))

cnttttt = 0
cunt = 0
for i in range(lengt):
    if i%2 == 0:
        print(lastre1[cnttttt])
        cnttttt += 1
    else:
        print(lastre2[cunt])
        cunt += 1
    

