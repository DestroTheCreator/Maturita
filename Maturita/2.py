from tkinter import *
import time
import random

root= Tk()

sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()


canvas = Canvas(root ,bg = 'grey', width = sirka , height = vyska)
canvas.place(x = -2, y = -2)

pol = [50,100,150,200]
god = random.choice(pol)
win = False

lbl = Label(root,text = '60',bg = 'gray',font = 25)
lbl.place(x= 700, y = 200)
laabel = Label(root,text = 'idk yet mate', font = 20 ,bg = 'gray')
laabel.place(x = 700,y= 100)
root.attributes("-fullscreen", True)
time = 60
def tick():
    canvas.delete(ALL)
    canvas.create_line(100,50,200,50,width = 20, fill = 'green')
    canvas.create_line(100,100,200,100,width = 20, fill = 'blue')
    canvas.create_line(100,150,200,150,width = 20, fill = 'red')
    canvas.create_line(100,200,200,200,width = 20, fill = 'yellow')
    global time
    time -= 1
    lbl.config(text=time)
    if time == 0:
        lbl.config(text = 'bum')
    else:
        canvas.after(1000, tick)
canvas.after(1, tick)
l = Label(text = '')
l.place(x = 800 ,y = 10)
def strih(event):
    global win
    global god
    a,b = event.x,event.y
    l.config(text = b)
    if a <= 200 and a >= 100:
        if b > 210:
            laabel.config(text = 'stlac caru')
        else:
            if (b <=60  and b >=40) or  (b <=110  and b >=90) or (b <=160  and b >=140) or (b <=210  and b >=190):
                if b >= god-10 and b <= god+10:
                    laabel.config(text = 'vyhral si')
                else:
                    laabel.config(text = 'skus znova')
            else:
                laabel.config(text = 'stlac caru')  
    else:
        laabel.config(text = 'stlac caru') 



ex = Button(root, text = 'die',command =  root.destroy)
ex.place(x=0,y=0)



root.bind('<Button-1>',strih)

mainloop()