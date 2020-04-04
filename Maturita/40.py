f = open('School/Maturita/texty/40.txt','r').read()

import re
cisla = re.findall(r'\d+',f)
cisla = [int(i)for i in cisla]



import numpy as np 
grid = (np.reshape(cisla,(9,10))).tolist()




lst = []

import time

class island:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.area = 0
    
    def expanse(self):
        global grid, lst
        up = True
        down = True
        right = True
        left = True
        next = []
        #first tile
        if (str(self.x)+'_'+str(self.y)) not in lst:
            a = 0
            self.area += 1
            next.append(self.x)
            next.append(self.y)
            next_copy = next
            while True:
                for i in range(len(next_copy)//2):
                    next = []
                    self.x = next_copy[i*2]
                    self.y = next_copy[2*i+1]
                    if (str(self.x)+'_'+str(self.y)) not in lst:
                        lst.append(str(self.x)+'_'+str(self.y))
                        #check ci moze do stran
                        if self.y == 0:
                            right = False
                        if self.y == len(grid[0])-1:
                            left = False
                        if self.x == 0:
                            up = False
                        if self.x == len(grid)-1:
                            down = False
                        print(lst)

                        #Getting next 4 tiles
                        if left:
                            if grid[self.x][self.y-1] != 0 and (str(self.x)+'_'+str(self.y-1)) not in lst:
                                next.append(self.x)
                                next.append(self.y-1)
                                self.area += 1
                        if right:
                            if grid[self.x][self.y+1] != 0 and (str(self.x)+'_'+str(self.y+1)) not in lst:
                                next.append(self.x)
                                next.append(self.y+1)
                                self.area += 1
                        if up:
                            if grid[self.x-1][self.y] != 0 and (str(self.x-1)+'_'+str(self.y)) not in lst:
                                next.append(self.x-1)
                                next.append(self.y)
                                self.area += 1
                        if down:
                            if grid[self.x+1][self.y] != 0 and (str(self.x+1)+'_'+str(self.y)) not in lst:
                                next.append(self.x+1)
                                next.append(self.y)
                                self.area += 1
                        
                    time.sleep(1)
                next_copy = next
                print(self.area,'\nnext:',next_copy)
                if a == self.area:
                    break
                else:
                    a = self.area
        


for row in range(len(grid)):
    for element in range(len(grid[row])):
        if grid[row][element] != 0:
            isle = island(row,element)
            isle.expanse()
            print('-------------')



from tkinter import *

root = Tk()

canvas = Canvas(root,bg = 'gray',height = 400,width = 400)
canvas.place(x = -2,y = -2)


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            color = 'blue'
        else:
            color = 'green'
        canvas.create_rectangle(50 + 20*j,50 + 20*i,50 + 20*j+20,50 + 20*i+20,fill=color)



mainloop()
