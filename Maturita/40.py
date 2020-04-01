f = open('School/Maturita/texty/40.txt','r').read()

import re
cisla = re.findall(r'\d+',f)
cisla = [int(i)for i in cisla]

#print(int(len(cisla))-int(cisla.count(0)))

import numpy as np 
cisla = (np.reshape(cisla,(9,10))).tolist()
#print(cisla)


maxx = 0
counter = 0
from tkinter import *

root = Tk()

sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()

canvas = Canvas(root , width = sirka , height = vyska, bg = 'gray')
canvas.place(x = -2 , y = -2)
root.attributes("-fullscreen",True)

ex = Button(root,text = 'EXIT',command = root.destroy)
ex.place(x = 0, y = 0)

def draw():
    size = 40
    for i in range(len(cisla)):
        for ii in range(len(cisla[i])):
            if cisla[i][ii] == 0:
                canvas.create_rectangle(100+size*ii,100+size*i,100+size+size*ii,100+size+size*i,fill = 'blue')
            else:
                canvas.create_rectangle(100+size*ii,100+size*i,100+size+size*ii,100+size+size*i,fill = 'darkgreen')

draw()

mainloop()
count = 0
velkosti = []
pouzite = []
def ostrov(array):
    global count,pouzite
    pouzite = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] != 0 and ((str(i)+'-'+str(j)) not in pouzite):
                count += 1
                pouzite.append(str(i)+'-'+str(j))
                try:
                    a = array[i][j-1]
                    aa = str(i)+'-'+str(j-1)
                except IndexError:
                    continue
                try:
                    b = array[i][j+1]
                    bb = str(i)+'-'+str(j+1)
                except IndexError:
                    continue
                try:
                    c = array[i-1][j]
                    cc = str(i-1)+'-'+str(j)
                except IndexError:
                    continue
                try:
                    d = array[i+1][j]
                    dd = str(i+1)+'-'+str(j)
                except IndexError:
                    continue
                vedlajsie = []
                vedl_sur = []
                try:
                        
                    if a != 0:
                        vedlajsie.append(a)
                        aa = str(i)+'-'+str(j-1)
                        vedl_sur.append(aa)
                        count+=1
                    if b != 0:
                        vedlajsie.append(b)
                        bb = str(i)+'-'+str(j+1)
                        vedl_sur.append(bb)
                        count+=1
                    if c != 0:
                        vedlajsie.append(c)
                        cc = str(i-1)+'-'+str(j)
                        vedl_sur.append(cc)
                        count+=1
                    if d != 0:
                        vedlajsie.append(d)
                        dd = str(i+1)+'-'+str(j)
                        vedl_sur.append(dd)
                        count+=1
                    helpcount = len(vedlajsie)
                    print(vedlajsie,vedl_sur)
                    '''while True:
                        if helpcount == 0:
                            break
                        for iksde in range(helpcount):
                            if (str(i)+'-'+str(j)) not in pouzite:
                                if a != 0:
                                    vedlajsie.append(a)
                                    aa = str(i)+'-'+str(j-1)
                                    count+=1
                                    helpcount += 1
                                if b != 0:
                                    vedlajsie.append(b)
                                    bb = str(i)+'-'+str(j+1)
                                    count+=1
                                    helpcount += 1
                                if c != 0:
                                    vedlajsie.append(c)
                                    cc = str(i-1)+'-'+str(j)
                                    count+=1
                                    helpcount += 1
                                if d != 0:
                                    vedlajsie.append(d)
                                    dd = str(i+1)+'-'+str(j)
                                    count+=1  
                                    helpcount += 1
                                    '''
                             

            

                        
                except IndexError:
                    pass







ostrov(cisla)






print(pouzite)
