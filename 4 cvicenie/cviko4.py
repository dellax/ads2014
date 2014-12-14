#uloha 1
#upravte testovanie vyhradzovanej pamäti (funkcia zisti() z prednášky) pre
#pythonovský append() (kde sa sleduje, pri akých hodnotách sa nafukuje vnútorné
#pole) funkciu upravte pre váš počítač

import sys

def zisti(n):
    pole = []
    size0 = 0
    for i in range(n):
        size = sys.getsizeof(pole)
        if size != size0:
            size0 = size
            print('len:{:4} sizeof:{:6}  {:3}'.format(len(pole), size, (size-36)//8))
        pole.append(None)

def uloha1():
    zisti(300)

#uloha 2
#na konci prednášky je príklad so spracovaním dlhého znakového reťazca
#so zložitosťou O(n**2)
#pomocou pomocného poľa sa úloha rieši so zložitosťou O(n)
#otestujte reálnu rýchlosť pre reťazce rôznych
#dĺžok (100000, 1000000, ..., 10000000)
#zistite, akú časť výpočtu tu zaberá operácia join()
#(porovnajte 3 rôzne rýchle verzie)

def ret1(ret):
    s2 = ''
    for znak in ret:
        s2 += znak

def ret2(ret):
    pom = []
    for znak in ret:
        pom.append(znak)
    s2 = ''.join(pom)
    
def uloha2(ret):
    import time
    start = time.time()
    ret1(ret)
    cas1 = time.time()-start

    start = time.time()
    ret2(ret)
    cas2 = time.time()-start

    print(cas1, cas2)

#uloha 3
#v prednáške sme skúmali použitú pamäť a rýchlosť metódy append()
#(amortizovaná zložitosť)
#zistite, ako sa mení použitá pamäť a priemerný čas pre operáciu
#list.pop(), skúmajte pre veľké polia

def priemer(n):
    import time, sys
    pole = []
    casy = []
    size0 = 0
    for i in range(n):
        pole.append(None)
    while len(pole) > 0:
        size = sys.getsizeof(pole)
        if size != size0:
            size0 = size
            print('len:{:4} sizeof:{:6}  {:3}'.format(len(pole), size, (size-36)//8))
        start = time.time()
        pole.pop()
        casy.append(time.time()-start)
    print('len:{:4} sizeof:{:6}  {:3}'.format(len(pole), size, (size-36)//8))    
    cas = 0
    for prvok in casy:
        cas += prvok
    cas /= len(casy)
    print("Priemerny cas na pop() je: {}".format(cas))

def uloha3(n):
    priemer(n)

#uloha 4
#do triedy DynamickePole dodefinujte metódu pop(self) - navrhnite
#vlastnú stratégiu, kedy a o koľko sa bude pole zmenšovať
#(napr. keď je vyhradená pamäť n využitá len na n/4, tak sa zmeší na n/2)
#otestujte ju rovnakými testami ako v úlohe (3)

import ctypes

class DynamickePole:
    def __init__(self):
        self.n = 0
        self.vyhr = 1
        self.pole = self.vyrob_pole(self.vyhr)

    def __len__(self):
        return self.n

    def __getitem__(self, ix):
        if not 0 <= x < self.n:
            raise IndexError('vadny index')
        return self.pole[ix]

    def __repr__(self):
        res = ''
        for i in range(self.n):
            res += ', ' + repr(self.pole[i])
        return 'dyn[' + res[2:] +']'

    def append(self, prvok):
        if self.n == self.vyhr:
            self.resize(2 * self.vyhr)
        self.pole[self.n] = prvok
        self.n += 1

    def pop(self):
        if self.n == self.vyhr / 2:
            self.resize(self.vyhr / 2)
        self.n -= 1

    def resize(self, nova):
        pole2 = self.vyrob_pole(nova)
        for i in range(self.n):
            pole2[i] = self.pole[i]
        self.pole = pole2
        self.vyhr = nova

    def vyrob_pole(self, d):
        return (d * ctypes.py_object)()

def priemer2(n):
    import time, sys
    pole = DynamickePole()
    casy = []
    size0 = 0
    for i in range(n):
        pole.append(None)
    while len(pole) > 0:
        size = pole.vyhr
        if size != size0:
            size0 = size
            print('len:{:4} sizeof:{:6}  {:3}'.format(len(pole), size, (size-36)//8))
        start = time.time()
        pole.pop()
        casy.append(time.time()-start)
    print('len:{:4} sizeof:{:6}  {:3}'.format(len(pole), size, (size-36)//8))    
    cas = 0
    for prvok in casy:
        cas += prvok
    cas /= len(casy)
    print("Priemerny cas na pop() je: {}".format(cas))

def uloha4(n):
    priemer2(n)

#uloha 5
#podobne ako sme v (3) skúmali pop (amortizovaná zložitosť)
#zistite, ako sa mení použitá pamäť a priemerný čas pre operáciu
#list.insert(k,...), skúmajte pre veľké polia

def priemer3(n):
    import time, sys
    pole = []
    casy = []
    size0 = 0
    while len(pole) != n:
        size = sys.getsizeof(pole)
        if size != size0:
            size0 = size
            print('len:{:4} sizeof:{:6}  {:3}'.format(len(pole), size, (size-36)//8))
        start = time.time()
        pole.insert(0, None)
        casy.append(time.time()-start)
    print('len:{:4} sizeof:{:6}  {:3}'.format(len(pole), size, (size-36)//8))    
    cas = 0
    for prvok in casy:
        cas += prvok
    cas /= len(casy)
    print("Priemerny cas na insert() je: {}".format(cas))

def uloha5(n):
    priemer3(n)

#uloha 6
#do triedy DynamickePole dodefinujte metódu insert(self, )
#otestujte ju rovnakými testami ako v úlohe (4)

#uloha 7
#zadefinujte triedu dvojrozmerné číselné pole a metódy pre
#inicializovanie veľkosti NxM: predpokladáme reprezentáciu poľa riadkov,
#napr. [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#zapísať do súboru (po riadkoch)
#prečítať zo súboru
#operácie súčet, rozdiel, násobenie konštantou
#testy či všetky nulové, počet nezáporných prvkov, či je symetrická, ...
#rozsekať dlhé pole na riadky a naopak z 2D poľa vyrobiť jedno dlhé pole

#uloha 8
#pomocou triedy zo (7) príkladu vytvoriť triedu Sudoku, ktorá
#skontroluje, či je kompletné riešenie
#či nie je kolízia v nedoriešenom sudoku: vo všetkých riadkoch, stĺpcoch, štvorcoch 3x3 musia byť rôzne čísla


    
