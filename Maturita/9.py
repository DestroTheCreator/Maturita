f = open('School/Maturita/texty/9.txt','r').read()
import re
zastavky = re.findall(r'[A-z]+[ ][A-z]+|[A-z]+',f)
print(zastavky,len(zastavky))
maxx = re.findall(r'[0-9]+[\n]',f)
mx = ''
for i in maxx:
    mx += i
mx = int(mx)
nastup = re.findall(r'[0-9]+',f)
print(nastup)
maxxx = 0
zmena = 1
obsadenost = 0
for i in range(len(zastavky)):
    obsadenost = obsadenost + int(nastup[zmena]) - int(nastup[zmena+1])
    zmena += 2
    if maxxx < obsadenost:
        maxxx = obsadenost
    if obsadenost > mx:
        print("Preplneny bus po zastavke",zastavky[i],".")
print (maxxx - mx)


