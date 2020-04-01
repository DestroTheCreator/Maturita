fiele = open('School/Maturita/texty/29.txt','r')
import re
veta = []
for i in range(sum(1 for line in open('School/Maturita/texty/29.txt'))):
    f = fiele.readline()
    a = re.findall(r'[A-Za-z0-9?!@#$%-^&*,.;:()]+',f)
    veta.append(''.join([(j[0].upper()+" ".join([x[1:] for x in j.split(" ")])) for j in a]))
print(veta)