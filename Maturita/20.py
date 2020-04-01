from tkinter import *
import random
root = Tk()

s = root.winfo_screenwidth()
h = root.winfo_screenheight()

c = Canvas(root,width = s, height = h)
c.place(x = -2 , y = -2)

root.attributes("-fullscreen", True)

x1 = 40
x2 = 40
y1 = 120
y2 = 300

lb = Label(root,text = 'vitaz?',font = 40)
lb.place(x = 750,y=0)

ryc = [1,3,5,7,9,15]


def move():
    c.delete("all")
    global x1
    global x2

    x1 += random.choice(ryc)
    x2 += random.choice(ryc)


    #Sachovnica
    for i in range(50):
        if i %2 ==0:
            c.create_rectangle(1280,1+20*i,1300,20+20*i,fill = 'black')
        else:
            c.create_rectangle(1280,1+20*i,1300,20+20*i,fill = 'white')
        
    for i in range(50):
        if i %2 ==0:
            c.create_rectangle(1300,1+20*i,1320,20+20*i,fill = 'white')
        else:
            c.create_rectangle(1300,1+20*i,1320,20+20*i,fill = 'black')
    

    c.create_rectangle(x1,y1,x1+100,y1+50,fill = "purple")
    c.create_oval(x1,y1+40,x1+40,y1+80,fill = "black")
    c.create_oval(x1+60,y1+40,x1+100,y1+80,fill = "black")

    c.create_rectangle(x2,y1+150,x2+100,y1+150+50,fill = "green")
    c.create_oval(x2,y1+150+40,x2+40,y1+150+80,fill = "black")
    c.create_oval(x2+60,y1+150+40,x2+100,y1+150+80,fill = "black")
    if x1 > 1200:    
        lb.config(text = "vitaz = 1")
        root.after_cancel()




    if x2 > 1200:
        lb.config(text = "vitaz = 2")
        root.after_cancel()
        

    root.after(20,move)




    
    



ex = Button(root, text = 'dead', command = root.destroy)
ex.place(x = 0,y =0)

move()




mainloop()
