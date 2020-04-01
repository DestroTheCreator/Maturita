from tkinter import *
import math


root = Tk()

sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()

c = Canvas(root,height = vyska , width = sirka,bg = 'gray')
c.place(x = -2,y = -2)

root.attributes("-fullscreen", True)

ex = Button(root, text='exit', command=root.destroy)
ex.place(x=sirka-30, y=0)

#-----------------------------------------------------------------------

angle = 270
radius = 300



def hodziny():
    global angle
    c.delete(ALL)
    angle += 0.06
    end_x = sirka/2 + radius * math.cos(math.radians(angle))
    end_y = vyska/2 + radius * math.sin(math.radians(angle))

    c.create_oval(sirka/2-radius,vyska/2-radius,sirka/2+radius,vyska/2+radius)

    c.create_line(sirka/2,vyska/2,end_x,end_y)

    c.create_text(sirka/2,vyska/2-radius-20,text = "12",font = 30)
    c.create_text(sirka/2,vyska/2+radius+20,text = "6",font = 30)

    c.create_text(sirka/2+radius+20,vyska/2,text = "3",font = 30)
    c.create_text(sirka/2-radius-20,vyska/2,text = "9",font = 30)

    root.after(10,hodziny)




root.after(1,hodziny)

mainloop()