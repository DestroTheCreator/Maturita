import re
f = open('School/Maturita/texty/5.txt','r')
filee = f.read()
new_file = re.sub(r'\n',' ',filee)
lst = re.findall(r'[hdpl\.]+',new_file)
print('pocet hier =',len(lst))
c = 1
mx = 0
mxx = 0
for game in lst:
    print('hra c.',c,' ma = ',len(game))
    if len(game) > mx:
        mx = len(game)
        mxx = c
    c+=1
print('najdlhsia hra = ',mxx,' s poctom znakov = ',mx)
lst2 = re.findall(r'[hdpl]',new_file)
arr = []
counter = 1
var = '  '
vi = ''
for i in lst2:
    if var == i:
        counter += 1
    elif var == '  ':
        var = i
    elif var == ' ':
        var = i
        arr.append(' ')
    else:
        vi = ''
        vi += var
        vi += str(counter)
        arr.append(vi)
        var = i
        counter = 1

vi = ''
vi += var
vi += str(counter)
arr.append(vi)

strr = ''
for i in arr:
    if i == ' ':
        strr += '\n'
    else:
        strr += i+' '
print(strr)
