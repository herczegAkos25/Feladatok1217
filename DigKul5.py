import random
szamok=[]
meredek_szakasz=0
visszafele=0

for i in range(30):
    szamok.append(random.randint(0,9))

for szam in szamok:
    if szamok[szam] - szamok[szam + 1] >= 2:
        meredek_szakasz += 1
for szam in szamok:
    if szamok[szam+1] - szamok[szam] >= 2:
        visszafele += 1

print(f"Meredek szakaszok száma az odafele vezető úton: {meredek_szakasz}")
print(f"Meredek szakaszok száma a visszaúton: {visszafele} ")