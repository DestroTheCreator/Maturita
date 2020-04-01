import re
f = open('School/Maturita/texty/23.txt','r').read()
ciselka = (re.findall(r'[0-9]+',f))
ciselka = [int(i) for i in ciselka]
print(len(ciselka))


def ciginigi(x):
    arr = []
    for j in range(len(ciselka)):
        i = ciselka[j]
        if int(x) == int(i):
            arr.append(j+1)
    return(arr)

for i in range(10):
    vas = '522'+str(i)
    print(ciginigi(vas))
    #skr = open('School/Maturita/texty/vas.txt','w')
    #skr.write(ciginigi(vas))







