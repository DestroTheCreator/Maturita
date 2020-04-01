import re
from tkinter import *
import random as rd
root = Tk()

s = root.winfo_screenwidth()
v = root.winfo_screenheight()

canvas = Canvas(root,width = s, height = v,bg = 'gray' )
canvas.place(x = -2,y = -2)


root.attributes("-fullscreen",True)


ex = Button(root,command = root.destroy)
ex.place(x= 0 ,y = 0)
#_____________________________________________________

kody = re.findall(r'[\d]+',(open('School/Maturita/texty/15.txt','r').read()))

randkod = [rd.randint(0,9)for i in range(8)]

x = 50
x2 = 60
y = 20
for i in range(8):
    if i == 0 or i == 7:
        canvas.create_rectangle(x,y,x+randkod[i],y+70,fill = 'black')
    else:
        canvas.create_rectangle(x,y,x+randkod[i],y+50,fill = 'black')
    canvas.create_text(x2,y+60,text = randkod[i])
    x += 11
    x2 += 9


x0 = 50
y0 = 120
x20 = 60
for i in kody:
    for j in range(8):
        if j == 0 or j == 7:
            canvas.create_rectangle(x0,y0,x0+int(i[j]),y0+70,fill = 'black')
        else:
            canvas.create_rectangle(x0,y0,x0+int(i[j]),y0+50,fill = 'black')
        canvas.create_text(x20,y0+60,text = i[j])
        x0 += 11
        x20 += 9
    x0 += 120
    x20 +=136


mainloop()
