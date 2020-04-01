from tkinter import *

root = Tk()
sirka = root.winfo_screenwidth()
vyska =root.winfo_screenheight()


canvas = Canvas(root , height = vyska,width = sirka,bg= "gray")
canvas.place(x = -2,y = -2)

root.attributes("-fullscreen",True)

ex = Button(root,text = 'exit',command =root.destroy)
ex.place(x =sirka - 27,y =0)
a = 21
def gomate():
    global a
    canvas.delete(ALL)
    canvas.create_rectangle(400,100,650,600,fill = "black")
    if a >10:
        canvas.create_oval(450,150,600,300,fill = 'green')
        canvas.create_text(525,225,text = a-11,font = 20)
    elif a<=10 and a > -1:
        canvas.create_oval(450,400,600,550,fill = 'red')
        canvas.create_text(525,475,text = a,font = 20)
    elif a == -1:
        a = 22
    a -=1
    root.after(1000,gomate)





root.after(1,gomate)


mainloop()