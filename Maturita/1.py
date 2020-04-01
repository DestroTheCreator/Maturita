from tkinter import *
import random
root = Tk()
sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()
s = sirka /10

lst = [s,s*2,s*3,s*4,s*5,s*6,s*7,s*8,s*9]

def shw(event):
    x,y = event.x,event.y
    if x >= asa and x <= asa+50:
        lbl.config(text = 'je')
    elif x > asa+50:
        lbl.config(text = 'vlavo')
    elif x < asa:
        lbl.config(text = 'vpravo')


    



root.attributes("-fullscreen",True)

canvas = Canvas(root , width = sirka , height = vyska, bg = 'gray')
canvas.place(x = -2 , y = -2)

lbl = Label(root,text = "estenic",font = 10)
lbl.place(x = 550 , y = 100)

ex = Button(root,text = 'gdsagasd',command = root.destroy)
ex.place(x = 0, y = 0)
asa = random.choice(lst)
canvas.create_rectangle(asa,500,asa+20,520,fill = 'green')

for i in range(9):
    canvas.create_oval(s*(i+1),480,s*(i+1)+50,530,fill = "blue")

root.bind('<Button-1>',shw)



mainloop()