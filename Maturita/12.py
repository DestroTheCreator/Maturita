from scipy import stats
string = input('')
a = []
for i in string:
    if i == ' ':
        print(0)
        a.append(0) 
    else:
        pismeno = ord(i)-65
        print(str(pismeno//3+1)*(pismeno%3+1))
        for j in range(pismeno%3+1):
            a.append(pismeno//3+1)

def mode(array):
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))
     
print(mode(a))
