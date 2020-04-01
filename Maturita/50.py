f = open('School/Maturita/texty/50.txt','r').read()
import re,numpy
hodnoty = re.findall(r'[-0-9]+',f)
hodnoty = [int(i)for i in hodnoty]

def avr(arr):
    return (sum(arr))/(len(arr))

print('min:',min(hodnoty),'\nmax:',max(hodnoty),'\npriemer:',avr(hodnoty))

hodnoty = numpy.reshape(hodnoty,(10,12))
hodnoty = hodnoty.tolist()
print(hodnoty)

stredy1 = []
stredy2 = []

for i in range(len(hodnoty)):
    stredy1.append(numpy.median(hodnoty[i]))
    stredy2.append(hodnoty[4][i])
print('zhora dole',avr(stredy1),'zprava dolava',avr(stredy2))