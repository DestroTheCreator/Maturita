import re
from tkinter import *

strng = open('School/Maturita/texty/8.txt','r').read()

hodnotenia = re.findall(r'nie|ano',strng)
god = re.findall(r'nie',strng)

print('hodnotenia_zle_:',len(god))


hodiny = re.findall(r'[0-9\.]+[:]',strng)
skr = []
for i in hodiny:
    hdz = re.sub(r':',' ',i)
    skr.append(hdz)

a = []
for i in skr:
    a.append(int(i))

counter = 0
for i in hodnotenia:
    if i == "ano":
        a.pop(counter)
    else:
        counter+=1

mx = 0
cnt = 0
mxx = ''
copy = ''
for i in a:
    if copy == i:
        cnt+=1
        if mx < cnt:
            mx = cnt
            mxx = i
    else:
        cnt = 0
    copy = i

print(mxx,'= najhejtovanejsia hodina s',mx+1,'zakaznikmi')




root = Tk()

canvas = Canvas(root, height = 400 , width = 520,bg = 'gray')
canvas.place(x= 20,y = -2)
ex = Button(root,command = root.destroy)
ex.place(x=0,y=0)
root.attributes("-fullscreen",True)

x=0
y=370


helparr = []
nextarr = []
cnterrjlskaf = 0
for i in range(len(a)):
    j = a[i]
    
    if j in helparr:
        cnterrjlskaf += 1

    else:
        nextarr.append(cnterrjlskaf+1)
        cnterrjlskaf = 0
    helparr.append(j)    
helparr = []
[helparr.append(x) for x in a if x not in helparr]

s = len(nextarr)
ss = 520/s
for i in range(len(nextarr)):
    ares = nextarr[i]
    canvas.create_rectangle(ss*i+2,y-ares*10,ss*i+ss-2,y)
    canvas.create_text(ss*i+ss/2,y+10,text = helparr[i])


mainloop()