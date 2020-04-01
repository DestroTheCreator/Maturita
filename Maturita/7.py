import re
f = open('School/Maturita/texty/7.txt','r').read()
mena = re.findall(r'[A-Za-z\.]+',f)
cas = re.findall(r'[0-9\.]+',f)

print('POcet zucanstenntch =',len(mena))    
for i in range(len(mena)):
    print('sutaziaci',mena[i],'dobehol do ciela za',cas[i],'sekund')

ma = min(cas)
ma = cas.index(ma)
print('best bol',mena[ma])
