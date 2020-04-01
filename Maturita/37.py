f = open('School/Maturita/texty/37.txt','r').read()
f = f.split('\n')
decs = []
for binary in f:
    decimal = 0
    for i in range(len(binary)):
        diget = int(binary[-i-1])
        decimal += int(diget*(2**i))
    decs.append(decimal)
print(decs)