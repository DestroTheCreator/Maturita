

veta = 'ahoj si moc borec a sick a kokot a jebe ti ndkfjaldf'
dlzka = len(veta)
arr = []
for i in range(1,17):
    arr.append(i*i)
    if i != 16:
        arr.append(i*(i+1))
print(arr)
rozdiel = 1000
for i in range(len(arr)):
    if dlzka-arr[i] < rozdiel and dlzka-arr[i] >= 0:
        rozdiel = dlzka-arr[i]
        ind = i+1
print(ind)
for i in range(1,17):
    if (i*i) == arr[ind]:
        a = i
        b = i
    if (i*(i+1)) == arr[ind]:
        a = i
        b = i+1


print(a,b) 
vypisi = [] 
for j in range(a):
    aasd = []
    for i in range(b):
        try:
            aasd.append(veta[i+(j*b)])
        except IndexError:
            aasd.append(' ')
    vypisi.append(aasd)
for riadok in vypisi:
    for prvok in riadok:
            print('', prvok, end='  ')
    print()
print('----------------------------------------------------------------')
import random
arrrr = [i for i in range(b)]
for iad in range(len(vypisi)//2):
    c = random.choice(arrrr)
    d = random.choice(arrrr)
    for i in range(len(vypisi)):
        vypisi[i][c],vypisi[i][d] = vypisi[i][d],vypisi[i][c]
for riadok in vypisi:
    for prvok in riadok:
            print('', prvok, end='  ')
    print()