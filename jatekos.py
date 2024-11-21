'''adattagok: nev, poz, kaszt, hp - nem kívülről kapja, hanem egy belső függvény adja majd meg.'''
import random
class jatekos():
    def __init__(self, nev:str="Játékos", poz:str=0, kaszt:str="Harcos", emo:str="h"):
        self.nev=nev
        self.poz=poz
        self.kaszt=kaszt
        self.emo=emo
        self.hp=3+random.randint(1,6)

    def set_pozicio(self):
        self.poz=random.randint(0,2)

    def set_hp(self):
        self.hp=self.hp-random.randint(0,1)

    def __str__(self):
        return f"Név: {self.nev}, Pozíció: {self.poz}, Kaszt: {self.kaszt}, Életerő: {self.hp}, Karakter: {self.emo}"