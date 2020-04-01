import re
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

f = open('School/Maturita/texty/33.txt','r').read()
pretekari = re.findall(r'\d\d\d ',f)
pretekari = [int(i) for i in pretekari]
casy = re.findall(r'\d+:\d+',f)
casy = [(''.join(i.split(':')))for i in casy]

stan = []
num_lines = sum(1 for line in open('School/Maturita/texty/33.txt'))
t = open('School/Maturita/texty/33.txt','r')
for k in range(num_lines):
    i = t.readline()
    stanovistia = re.findall(r'[[][,\d]+[]]',i)
    stan.append(stanovistia)

dojebky = []
for i in range(len(pretekari)):
    koberce = stan[i]
    if len(koberce) == 5:
        pass
    else:
        print(pretekari[i],'to dojebal a netrafil stanovistia secky')
        dojebky.append(i)

for i in dojebky:
    pretekari.pop(i)
    casy.pop(i)
    stan.pop(i)
print('fast boi je',pretekari[casy.index(min(casy))])