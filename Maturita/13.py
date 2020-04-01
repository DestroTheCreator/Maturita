import re
f = open('School/Maturita/texty/13.txt','r').read()
arr = []
fil = re.findall(r'[A-Za-z]+',f)
for word in fil:
    w = (word.lower())
    arr.append(w)

string = ''

for i in arr:
    string +=i
print(string)
rere = re.findall(r'[a-z]',string)
helpiarr = []
cnt = 0
helpi = []
abeceda= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for iksde in range(len(abeceda)):
    j = abeceda[iksde]
    sree = (j+':'+str(rere.count(j)))
    helpi.append(sree)
print(helpi)
    




