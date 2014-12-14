#Uloha 1
#Naprogramujte insert_sort(pole), ktorý triedi priamo pole bez pomocnej pamäti
#zistite, aké najväčšie pole sa dá týmto triedením utriediť
#za 1 sekundu a za 2 sekundy
#odhadnite počet inštrukcií pre vykonanie tohto
#triedenia(v najhoršom prípade) pre pole s n-prvkami

def insert_sort(pole):
    for i in range(1, len(pole)):
        p = pole[i]
        j = i-1
        while j >= 0 and pole[j] > p:
            pole[j+1] = pole[j]
            j -= 1
        pole[j+1] = p

def uloha1():
    import random, time
    n = 2300 #1s ~ 2400prvkov, 2s ~ 3300prvkov
    pole = []
    for i in range(n):
        pole.append(random.randrange(10000))
    start = time.time()
    insert_sort(pole)
    cas1 = time.time()-start
    print(cas1)

#Uloha3
#Napíšte druhú verziu tohto triedenia, v ktorom sa zaraďovanie prvku
#na správne miesto utriedenej časti poľa použije metóda list.insert() a
#vyhodenie prvku pomocou del
#odhadnite počet inštrukcií pre vykonanie tohto
#triedenia (v najhoršom prípade) - treba nejako odhadnúť metódu
#insert a príkaz del
#aké najväčšie pole sa dá teraz utriediť za 1 sekundu a za 2 sekundy

def insert_sort2(pole):
    for i in range(1, len(pole)):
        j = i-1
        while j >= 0 and pole[j] > pole[i]:
            j -= 1
        pole.insert(j+1,pole[i])
        del pole[i+1]

def uloha2():
    import random, time
    n = 3300 #1s ~ 2400prvkov, 2s ~ 3300prvkov
    pole = []
    for i in range(n):
        pole.append(random.randrange(10000))
    start = time.time()
    insert_sort(pole)
    cas1 = time.time()-start
    print(cas1)

#Uloha 3
#navrhnite funkciu test(), pomocou ktorej budete merať rýchlosť vykonávania
#rôznych algoritmov triedenia:
#prvým parametrom bude veľkosť poľa - váš algoritmus vygeneruje náhodné
#pole a toto sa použije pre rôzne verzie algoritmu
#program potom postupne spustí triedenie pre všetky zadané verzie algoritmu
#s tým istým poľom
#odmeria čas a skontroluje správnosť utriedenia poľa (môžete použiť
#funkciu sorted())
#tretím parametrom je počet opakovania jedného testu, t.j. všetko sa to
#spustí príslušný počet krát a celkový čas sa vydelí týmto počtom
#na záver vypíše tabuľku: číslo algoritmu, (priemerný) čas trvania, 
#správnosť utriedenia (True/False)

def bubble_sort(pole):
    for i in range(len(pole)):
        for j in range(len(pole)-1):
            if pole[j+1] < pole[j]:
                pole[j], pole[j+1] = pole[j+1], pole[j]
                
def quick_sort(pole):
    def rozdel(z,k):   # vrati poziciu pivota
        'rozdeli pole na 2 casti'
        pivot = pole[z]
        index = z
        for i in range(z+1,k+1):
            if pole[i] < pivot:
                index += 1
                pole[i],pole[index] = pole[index],pole[i]
        pole[z],pole[index] = pole[index],pole[z]
        return index

    def quick_sort1(z, k):
        if z < k:
            index = rozdel(z,k)
            quick_sort1(z, index-1)
            quick_sort1(index+1, k)

    quick_sort1(0, len(pole)-1)

def test(n, zoznam_algoritmov, pocet_testov=1):
    import random, time
    spravnost = [True]*len(zoznam_algoritmov)
    casy = [0]*len(zoznam_algoritmov)
    for i in range(pocet_testov):
        polia = []
        gen = []
        for p in range(n):
            gen.append(random.randrange(10000))
        for m in range(len(zoznam_algoritmov)):
            polia.append([]+gen)
            start = time.time()
            zoznam_algoritmov[m](polia[m])
            casy[m] += time.time()-start
            if (polia[m] != sorted(gen)): spravnost[m] = False
    for cas in casy:
        cas /= pocet_testov
    for i in range(len(zoznam_algoritmov)):
        print("algorytmus {}: cas = {}, spravnost = {}".format(i,casy[i],spravnost[i]))
            

def uloha3():
    test(1000,[quick_sort, insert_sort, insert_sort2, bubble_sort],5)

#uloha 4
#ďalšia verzia tohto triedenia bude postupne vytvárať nové utriedené pole,
#do ktorého bude vkladať (zreťazovaním polí) ďalšie prvky na správne miesto
#a na záver obsoh tohto utriedeného pomocného poľa prekopíruje do formálneho
#parametra funkcie
def insert_sort3(pole):
    pom = [pole[0]]
    i = 1
    for prvok in pole[1:]:
        # nájdi index ix v pom, kam zaradiť prvok
        ix = i-1
        while ix >= 0 and prvok < pom[ix]:
            ix -= 1
        i += 1
        ix += 1
        pom = pom[:ix] + [prvok] + pom[ix:]
    # kopíruj pom do pole
    for i in range(len(pole)):
        pole[i] = pom[i]

def uloha4():
    test(1000,[insert_sort, insert_sort2, insert_sort3],5)

#Uloha 5 DOKONCIT
#Naprogramujte funkciu, ktorá utriedi spájaný zoznam - funkcia
#nebude meniť hodnoty atribútu info ale len next
#môžete použiť ľubovoľné triedenie, napr. min-sort

class Zoznam():
    class _Vrchol():
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next

    def __init__(self):
        self.zac = None

    def pridaj(self, data):
        if self.zac == None:
            self.zac = self._Vrchol(data)
        else:
            pom = self.zac
            while pom.next is not None:
                pom = pom.next
            pom.next = self._Vrchol(data)

    def daj_pole(self, point = None):
        if point is not None: pom = point
        else: pom = self.zac
        pole = []
        while pom is not None:
            pole.append(pom.data)
            pom = pom.next
        return pole

    def min_sort(self):
        import time
        if self.zac is not None:
            start = self.zac
            najmensi = False
            i = 0
            while True:
                j = i
                pom = start
                print(self.daj_pole(pom))
                while j > 0 or pom is not None:
                    pom = pom.next
                    j -= 1
                if j == i: break
                
                
                time.sleep(1)
                minimalny = pom
                predch = pom
                while pom is not None:
                    if minimalny.data > pom.data:
                        minimalny = pom
                        prev = predch
                i += 1
                prev.next = minimalny.next
                minimalny.next = start.next
                start = minimalny
                
                    

if __name__ == "__main__":
    zoz = Zoznam()
    for i in range(10):
        zoz.pridaj(10-i)
    print("ok")
    pole = zoz.daj_pole()
    print(pole)
    zoz.min_sort()
    pole = zoz.daj_pole()
    print(pole)
    
    
   
