
"""A játékban van egy harcos és egy varázsló, akik minden körben egy 3 elemű játéktéren léphetnek véletlenszerűen egy mezőre. Amennyiben ugyanarra a mezőre lépnek, akkor harcolnak.
Kezdetben mindkét játékos életerejét véletlenszerűen határozzuk meg egy 6 oldalú kocka dobásával. A minimális életerőpont 3 lehet, ehhez adjuk a kockadobás eredményét.
A játék során minden körben véletlenszerűen változik a játékosok pozíciója ([0,2] zárt intervallumban)
A harc azt jelenti, hogy az életerejük 0-val, vagy 1-gyel csökken."""

'''Milyen osztályok kellenek?
Jatekos()
adattagok: nev, poz, kaszt, hp - nem kívülről kapja, hanem egy belső függvény adja majd meg.

'''
from jatekos import jatekos
harcos=jatekos("Tubamtolog",0,"támogató","🦸‍♂️")
varazslo=jatekos("Waar'Ash Low",2,"varázsló","🧙‍♂️")

lista=["_","_","_"]
lista[harcos.poz]=harcos.emo
lista[varazslo.poz]=varazslo.emo
'''print(lista)

print(harcos)
print(varazslo)'''

def kiir(kor:int=0):
    print(f"{kor}. kör")
    print("*"*15,"  ","-"*27,"  ","-"*29,"  ")
    print(f"* {lista[0]:<3} {lista[1]:^3} {lista[2]:>3} *    | {harcos.nev} életereje: {harcos.hp} |    | {varazslo.nev} életereje : {varazslo.hp} |")
    print("*"*15,"  ","-"*27,"  ","-"*29,"  ")
    print("")

n=1

while (harcos.hp>0 and varazslo.hp > 0):
    harcos.set_pozicio()    #lép a harcos
    varazslo.set_pozicio()  #lép a varázsló
    lista=["_","_","_"]
    lista[harcos.poz]=harcos.emo
    lista[varazslo.poz]=varazslo.emo
    if (harcos.poz==varazslo.poz):
        lista[varazslo.poz]="⚔"
        harcos.set_hp()
        varazslo.set_hp()
    kiir(n)
    input()
    n+=1

if (harcos.hp==0):
    print(f"{varazslo.nev} nyert!")
else:
    print(f"{harcos.nev} nyert!")