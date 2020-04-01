import re, random

f = open('School/Maturita/texty/25.txt','r').read()

slova = re.findall(r'[A-z]+',f)
current_word = random.choice(slova)
print('.'*len(current_word),'\nHadaj pismena') 

zle = None
win = False
cnt = 0
listi = [('.') for i in range(len(current_word))]

while not win:
    zle = True
    inp = input()  
    for i in range(len(current_word)):
        if str(inp) == str(current_word[i]):
            listi[i] = inp
            zle = False

    if zle:
        cnt += 1 

    for ii in listi:
        print(ii,end='')
    print(cnt)

    if cnt == 10:
        print('prehral si')
        break
    if '.' not in listi:
        print('vyhral si')
        break
    






