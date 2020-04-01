import re
slova = re.findall(r'[A-z]+',open('School/Maturita/texty/24.txt','r').read())
ang = []
svk = []
for i in range(len(slova)):
    if i%2 != 0:
        ang.append(slova[i])
    else:
        svk.append(slova[i])

user_input = input('zadaj jazyk: ang alebo svk? ')
cnter = 0
if user_input == svk:
    while svk != []:
        print(svk[0],end ='=')
        a  = input()
        if str(a) == str(ang[0]):
            ang.pop(0)
            svk.pop(0)
        else:
            svk.append(svk[0])
            ang.append(ang[0])
            svk.pop(0)
            ang.pop(0)
            cnter += 1
else:
    while svk != []:
        print(ang[0],end ='=')
        a  = input()
        if str(a) == str(svk[0]):
            ang.pop(0)
            svk.pop(0)
        else:
            svk.append(svk[0])
            ang.append(ang[0])
            svk.pop(0)
            ang.pop(0)  
            cnter += 1
print('chyby:',cnter)

