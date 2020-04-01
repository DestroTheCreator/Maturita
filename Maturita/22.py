import random, re

f = open('School/Maturita/texty/22.txt','r').read()
print(f)

text  = re.findall(r'[A-Z][ a-z]+',f)
lst = []
for i in text:
    slova = re.findall(r'[A-z]+',i)
    lst.append(slova)
print(lst)
skus = [False,True]
if random.choice(skus) == True:
    random.shuffle(lst)

arr = []

for i in lst:
    outarr = []
    if random.choice(skus) == True:
        random.shuffle(i)
    for j in i:
        if random.choice(skus) == True:
            j = j[::-1]  
            outarr.append(j)
        else:
            outarr.append(j)
    arr.append(outarr)

print(arr)



