import re

f = open('School/Maturita/texty/45_1.txt','r').read()
f2 = open('School/Maturita/texty/45_2.txt','r').read()


from tkinter import *

root = Tk()
sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()

root.attributes("-fullscreen",True)

canvas = Canvas(root , width = sirka , height = vyska, bg = 'gray')
canvas.place(x = -2 , y = -2)



ex = Button(root,text = 'gdsagasd',command = root.destroy)
ex.place(x = 0, y = 0)



mainloop()