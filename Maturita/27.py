f = open('School/Maturita/texty/27.txt','r').read()

import re
dlzky = re.findall(r'\d+',f)

fi = open('School/Maturita/texty/27.txt','r')
pocet = fi.readline()
pocet = len(re.findall(r'\d+',pocet))

print('pocet miest je',pocet)

celk = (list(dict.fromkeys(dlzky)))
celk = [int(i) for i in celk]
print('celkova dlzka je:',sum(celk))

dlzky = [int(i)for i in dlzky]
m = max(dlzky)
for ii in range(len(dlzky)):
    i = dlzky[ii]
    if i == m:
        print((ii//pocet)+1)
