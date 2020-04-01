f = open('School/Maturita/texty/35.txt','r').read()
text = ''
znaky = [' ','.',',','!','?']
for i in f:
    for pismeno in i:
        if pismeno in znaky:
            pass
        else:
            pismeno = chr(ord(pismeno)-1)
        text+=pismeno
print(text)

'''
xd = open('School/Maturita/texty/rozsifrovane.txt','w')
xd.write(text)
'''