teren1 = int(input('teren1'))
teren2 = int(input('teren2'))  

from tkinter import *
import random as rd

root = Tk()
sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()

root.attributes("-fullscreen",True)

canvas = Canvas(root , width = sirka , height = vyska, bg = 'gray')
canvas.place(x = -2 , y = -2)

a = [0,1,-1]
lst = []
ex = Button(root,text = 'gdsagasd',command = root.destroy)
ex.place(x = 0, y = 0)

kopce = 0
diery = 0

for j in range(teren1):
    for i in range(teren2):
        c = rd.choice(a)
        lst.append(c)
        if c ==1:
            canvas.create_rectangle(500+50*i,200+50*j,500+50*i+50,200+50*j+50,fill = 'black')
            diery+=1
        if c == -1:
            canvas.create_rectangle(500+50*i,200+50*j,500+50*i+50,200+50*j+50,fill = 'green')
            kopce +=1
        else:
            canvas.create_rectangle(500+50*i,200+50*j,500+50*i+50,200+50*j+50)

canvas.create_text(140,40,text = 'chyba '+str(diery-kopce)+' furikov')
mainloop()