import re, random
lst = []
for i in range(10):
    a = random.randint(1,10)
    b = random.randint(1,10)
    c =[a,b,a*b]
    lst.append(c)
cnt = 0
points = 0
outputarr = []
while not lst == []:
    priklad = str(lst[0][0])+'*'+str(lst[0][1])+'='
    if cnt < 10:
        outputarr.append(priklad)
    ans = int(lst[0][2])
    print(priklad,end = '')
    user_ans = int(input())
    if user_ans == ans:
        if cnt < 10:
            points += 1
        lst.pop(0)
    else:
        ahah = lst.pop(0)
        lst.append(ahah)
    cnt += 1
print('ziskal si:',points,'bodov')
print(outputarr)

