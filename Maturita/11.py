import re
import numpy as np
f = open('School/Maturita/texty/11.txt','r').read()
mena = re.findall(r'[A-Za-z ]+[\n]',f)
mena = [re.sub('\n','',i) for i in mena]
aaa = len(mena)//2
m = []
for i in range(aaa):
    m.append(str(mena[i])+' '+str(mena[i+aaa]))
print(m)
mx = 0
mena = np.reshape(mena,(2,4))
for j in mena:
    for k in j:
        maaa = len(k)
        if ' ' in k:
            maaa -=1
        if maaa > mx:
            mx = maaa
    print(mx)



