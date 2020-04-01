import re
from tkinter import *


skr = '(a+b)-((()a-b)*2)'
zatvorky = re.findall(r'[()]',skr)
ln = len(zatvorky)
ano = ''
if len(zatvorky)%2 == 0:
    for i in range (int(ln/2)):
        x = (zatvorky[i], zatvorky[-i])
        if zatvorky[i] == zatvorky[-i]:
            ano = 0
        elif x == (')', '('):
            ano = 0
        else:
            ano = 1

farvy = ['blue','red','yellow','green','grey','pink']

root = Tk()

countre = 0
ct =0
if ano == 1:
    for i in skr:
        if i == '(' or i == ')':
            if i == '(':
                l = Label(root,text = i,fg = farvy[countre])
                l.place(x= ct,y=0)
                countre +=1
            elif i == ')':
                countre -=1
                l = Label(root,text = i,fg = farvy[countre])
                l.place(x= ct,y=0)
                

        else:
            l = Label(root,text = i,fg = 'black')
            l.place(x= ct,y=0)
        

        ct += 10
else:
    asd = Label(root,text = 'napcu')
    asd.place(x= ct,y=0)
        
        

mainloop()
