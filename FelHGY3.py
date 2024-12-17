import random

szamok=[]
nagyobb_0=0
kisebb_0=0
talalat=False

for index in range(100):
    szamok.append(random.randint(-100,100))

for szam in szamok:
    if szam > 0:
        nagyobb_0 += 1
    elif szam < 0:
        kisebb_0 += 1

for szam in szamok:    
    if szam > 50:
        print(f"50-nél nagyobb szám indexe: {szamok.index(szam)}")
        talalat=True
        break
if talalat == False:
    print(f"Nincs 50-nél nagyobb szám!")

# segítséggel:
for kulonbsegek in range(99): 
    if (szamok[kulonbsegek] - szamok[kulonbsegek + 1] > 120) or (szamok[kulonbsegek + 1] - szamok[kulonbsegek] > 120):
        print(f"Van olyan eset, hogy a két egymást követő szám különbsége meghaladja a 120-at")
        break
    else:
        print(f"Nincs olyan eset, hogy a két egymást követő szám különbsége meghaladja a 120-at")

if nagyobb_0 > kisebb_0:
    print(f"Több pozitív szám van")
else:
    print(f"Több negatív szám van")
    



