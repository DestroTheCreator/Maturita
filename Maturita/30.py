import re
vyska = float(input('daj vysku'))
koeficient = float(input('daj koeficient'))
counter = -1
for i in range(1000):
    if vyska > 1:
        counter += 1
        if i <=10:
            print(i,':',round(vyska,2),'m')
    else:
        if i <=10:
            print(i,':',round(vyska*100,1),'cm')
    vyska *= koeficient 
print(counter)