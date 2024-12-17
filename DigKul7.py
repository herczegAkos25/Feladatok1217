import random
szamok=[]
kint_a_vízbol=0
vizben=0
viz_felett=0
repulése=0

for i in range(80):
    szamok.append(random.randint(-5,3))

print(szamok)

for szam in szamok:
    if szam > 0:
        kint_a_vízbol+=1
    elif szam <= -1:
        vizben+=1
print(f"A delfin az út {(kint_a_vízbol+vizben)*80/100}%-t töltötte a vízben és víz felett!")

for szam in szamok:
    if kint_a_vízbol > vizben:
        print(f"A delfin többet volt kint a vízből, mint a víz alatt")
        break
    else:
        print(f"A delfin többet volt a vízben, mint a víz felett") 
        break

for szam in szamok:
    if szam >= 1:
        viz_felett+=1
        if viz_felett>repulése:
            repulése=viz_felett
    else:
        viz_felett=0
print(f"Ilyen hosszú volt a legnagyobb repülés: {repulése}")

