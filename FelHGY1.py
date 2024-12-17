szokoz=0
leghosszabb_szo=""
legtobb_szokoz=0

for index in range(5):
    mondat=input("Írj egy mondatot: ")

    for betuk in mondat:
        if betuk == " ":
            szokoz+=1
    if legtobb_szokoz < szokoz:
        leghosszabb_szo=mondat
        legtobb_szokoz=szokoz
    szokoz=0
print(f'A legtöbb szóközt tartalmazó mondat: {leghosszabb_szo}')