import re,random
from tkinter import *

f = open('School/Maturita/texty/21.csv','r').read()
mena = re.findall(r'[,][A-Za-z]+',f)
priezviska = re.findall(r'[A-Za-z]+[,]',f)
mena = [re.sub(',','',i) for i in mena]
priezviska = [re.sub(',','',i) for i in priezviska]

root =Tk()

h = root.winfo_screenheight()
w = root.winfo_screenwidth()

canvas = Canvas(root,width = w,height = h,bg = 'gray')
canvas.place(x = -2,y = -2)

ex = Button(root,text = 'exitbutton',bg = 'blue',fg = 'yellow',command = root.destroy)
ex.place(x = 0, y = 0)

root.attributes('-fullscreen',True)

l1 = Label(root,text = 'rady')
l1.place(x = 0, y = h-h//10-20)

l2 = Label(root,text = 'todruhe')
l2.place(x = 0, y = h-h//10+20)

e1 = Entry(root)
e1.place(x = 0,y = h-h//10)
e1.insert(0, "")

e2 = Entry(root)
e2.place(x = 0,y = h-h//10+40)
e2.insert(0,'')

a = b = None
def geti():
    global a,b
    a = int(e1.get())
    b = int(e2.get())


def kresli():
    if a*b >= len(mena):
        for j in range(b):
            for i in range(a):
                canvas.create_rectangle(200+i*((w-200)//a),50+j*((h-50)//b),50+i*((w-200)//a)+300,50+j*((h-50)//b)+80)
                try:
                    if len(mena) == 1:
                        cs = 0
                    else:
                        cs = random.randint(0,len(mena)-1)
                    canvas.create_text(200+i*((w-200)//a)+50,50+j*((h-50)//b)+10,text = priezviska[cs],fill = 'red')
                    canvas.create_text(200+i*((w-200)//a)+50,50+j*((h-50)//b)+45,text = mena[cs],fill = 'black')
                    mena.pop(cs)
                    priezviska.pop(cs)
                except Exception:
                    pass
    else:
        canvas.create_text(w//2,h//2,text = 'malo lavic')


but = Button(root,text = 'potvrd',command = lambda:[geti(),kresli()])
but.place(x = 125,y = h-h//10+40)

mainloop()