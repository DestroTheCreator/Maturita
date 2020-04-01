import re
arr = [40,50,20,70,30,30,40,0,50,100,20,200,30,50]
varr = []
sarr = []

for i in range(len(arr)):
    if i%2 == 0:
        sarr.append(arr[i])
    else:
        varr.append(arr[i])   

from tkinter import *
root = Tk()

v = root.winfo_screenheight()
s = root.winfo_screenwidth()



canvas = Canvas(root, height = v , width = s,bg = 'gray')
canvas.place(x= -2,y = -2)

ex = Button(root,text = 'E X I T',bg = 'gray',command = root.destroy)
ex.place(x=0,y=0)

root.attributes("-fullscreen",True)

radius = varr[0]
start = 540

for j in range(len(sarr)):
    if varr[j] == 0:
        canvas.create_line(start + radius, 700 - varr[j], start + radius + sarr[j], 700, fill = 'Green', width = 2)
    else:
        canvas.create_rectangle(start+radius, 700-varr[j], start+radius+sarr[j], 700)
    if j == 0 :
        pass
    elif varr[j] > varr[j-1]:
        canvas.create_line(start + radius, 700 - varr[j-1], start+radius, 700 - varr[j], fill = 'Red', width = 2)
        canvas.create_line(start + radius+sarr[j], 700 - varr[j], start+radius+sarr[j], 700 - varr[j+1], fill = 'Red', width = 2)
    radius += sarr[j]








mainloop()





















