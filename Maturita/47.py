f = open('School/Maturita/texty/47.txt','r').read()
import re
import random
kody = re.findall(r'\d+',f)
kody = [str(i)for i in kody]
asa = ''
for i in range(8):
    a = random.randint(1,9)
    asa += str(a)
print(asa,end = ' ')
h = [asa[0],asa[1],asa[2],asa[3]]
h = [int(i)for i in h]

g = [asa[2],asa[3],asa[4],asa[5]]
g = [int(i)for i in g]

w = [asa[4],asa[5],asa[6],asa[7]]
w = [int(i)for i in w]

print(int(str(sum(h)%2)+str(sum(g)%2)+str(sum(w)%2),2))

for i in kody:
    kod = i[:8]
    h = [kod[0],kod[1],kod[2],kod[3]]
    h = [int(i)for i in h]

    g = [kod[2],kod[3],kod[4],kod[5]]
    g = [int(i)for i in g]

    w = [kod[4],kod[5],kod[6],kod[7]]
    w = [int(i)for i in w]
    testi = int(str(sum(h)%2)+str(sum(g)%2)+str(sum(w)%2),2)
    if int(testi) != int(i[8]):
        print(kod,'nesedi s ',i[8],'..ma byt ',testi)