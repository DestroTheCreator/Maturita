f=open('School/Maturita/texty/14.txt','r').read()

import re
import random
user_input = input('daj cisla')

cisla = re.findall(r'[\d]+',user_input)
cisla = [(int(i))for i in cisla]
nahodnecisla = [random.randint(1,49) for i in range(6)]

print(cisla)
print(nahodnecisla)
for i in cisla:
    if i in nahodnecisla:
        print('uhadnute =',i)
    else:
        pass

loteri = re.findall(r'[0-9]+',f)

import numpy as np 
loteri = np.reshape(loteri,(7,6))
cnt = 0
for k in range(len(loteri)):
    j = loteri[k]
    cnt = 0
    for cisleo in range(len(j)):
        cis = int(j[cisleo])
        if cis in nahodnecisla:
            cnt += 1
    print(k+1,'. ','uhadol',cnt)
