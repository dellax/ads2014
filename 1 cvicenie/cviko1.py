#Uloha 1
#Zrealizujte dve verzie realizácie zásobníka:
#verzia pomocou poľa a operácií append(data) a pop()
#verzia pomocou jednosmerného spájaného zoznamu: pridávanie aj uberanie zo začiatku zoznamu
#Otestujte rýchlosť oboch realizácií.
class Stack_klasicky():
    def __init__(self):
        self.pole = []
    def pridaj(self, data):
        self.pole.append(data);
    def vyber(self):
        try:
            return self.pole.pop();
        except:
            return None
    def daj_prvok(self):
        return self.pole[-1]
    def is_empty(self):
        if len(self.pole) == 0:
            return True
        return False

class Stack_spajany():
    class _Prvok():
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next;
    def __init__(self):
        self.zac = None
    def pridaj(self, data):
        if self.zac is None:
            self.zac = self._Prvok(data)
        else:
            pom = self._Prvok(data)
            pom.next = self.zac
            self.zac = pom
    def vyber(self):
        if self.zac:
            pom = self.zac.data
            self.zac = self.zac.next
            return pom
    def daj_prvok(self):
        return self.zac.data
    def is_empty(self):
        if self.zac is None:
            return True
        return False

def uloha1():
    import random, time
    a = Stack_klasicky()
    b = Stack_spajany()
    n = 100000
    cas = time.time()
    for i in range (n):
        a.pridaj(random.randrange(1000))
    for i in range (n):
        a.vyber()
    koniec_Stack_klasicky = time.time()-cas
    cas = time.time()
    for i in range (n):
        b.pridaj(random.randrange(1000))
    for i in range (n):
        b.vyber()
    koneic_Stack_spajany = time.time()-cas
    print("Casy:\nKlasicke pole:{}\nSpajany zoznam:{}".format(koniec_Stack_klasicky, koneic_Stack_spajany))

#Uloha 2
#algoritmus triedenia daného poľa pomocou dvoch zásobníkov (rovnakého typu):
#najprv sa celé pole vloží (push) do prvého zásobníka
#postupne sa vyberajú všetky prvky (pop) a vkladajú sa do druhého pričom,
#vždy máme vybraté 2 prvky a vkladáme do druhého ten menší z nich
#keď sa prvý zásobník vyprázdni, prehadzujú sa prvky z druhého do prvého
#ale do zásobníka sa vkladá nie menší, ale váčší z nich
#toto sa celé opakuje, kým nezistíme, že všetky prvky sú už dobre utriedené,
#vtedy sa prvky vyberú späť do poľa

def utried(pole,typ):
    plni_sa = 2
    if typ == "python":
        s1 = Stack_klasicky()
        s2 = Stack_klasicky()
    else:
        s1 = Stack_spajany()
        s2 = Stack_klasicky()
    temp = []
    for prvok in pole:
        s1.pridaj(prvok)
    while True:
        if plni_sa == 1:
            utriedene = True;
            while not s2.is_empty():
                prvok1 = s2.vyber()
                prvok2 = s2.vyber()
                if prvok1 is None:
                    if prvok2 is None:
                        break
                    else:
                        s1.pridaj(prvok2)
                        break
                if prvok2 is None:
                    if prvok1 is None:
                        break
                    else:
                        s1.pridaj(prvok1)
                        break
                if prvok1 < prvok2:
                    utriedene = False;
                if prvok1 > prvok2:
                    s1.pridaj(prvok1)
                    s2.pridaj(prvok2)
                else:
                    s1.pridaj(prvok2)
                    s2.pridaj(prvok1)
            
            if utriedene: break
            plni_sa = 2
            
        elif plni_sa == 2:
            while not s1.is_empty():
                prvok1 = s1.vyber()
                prvok2 = s1.vyber()
                if prvok1 is None:
                    if prvok2 is None:
                        break
                    else:
                        s2.pridaj(prvok2)
                        break
                if prvok2 is None:
                    if prvok1 is None:
                        break
                    else:
                        s2.pridaj(prvok1)
                        break
                if prvok1 < prvok2:
                    s2.pridaj(prvok1)
                    s1.pridaj(prvok2)
                else:
                    s2.pridaj(prvok2)
                    s1.pridaj(prvok1)
            plni_sa = 1
    while not s1.is_empty():
        temp.append(s1.vyber())
    return temp

#Uloha 3
#otestujete správnosť a rýchlosť oboch realizácií
#zásobníka na tých istých vygenerovaných dátach
#(napr. 1000 náhodných celých čísel) - použite algoritmus triedenia (2)       
def uloha3():
    import random, time
    print("Test jednoducheho pola")
    pole = [10,1,58,1,25,14,24,1,0]
    nove1 = utried(pole,"python")
    nove2 = utried(pole,"spajany_zoznam")
    print("povodne pole: ",pole)
    print("python stack: ",nove1)
    print("spajany zoznam: ",nove2)
    if nove1 == nove2:
        print("Triedenie je spravne, pole1 == pole2")
    print("Generujem pole...")
    velke_pole = []
    n = 1000
    for i in range(n):
        velke_pole.append(random.randrange(10000))
    print("Triedim...")
    start = time.time()
    nvelke_pole1 = utried(velke_pole,"python")
    koniec1 = time.time()-start
    nvelke_pole2 = utried(velke_pole,"spajany_zoznam")
    koniec2 = time.time()-start
    if nvelke_pole1 == nvelke_pole2:
        print("Triedenie je spravne, nvelke_pole1 == nvelke_pole2")
    print("Casy utriedenia {} prvkoveho pola:\nPython stack = {}\nSpajany zoznam = {}".format(n,koniec1,koniec2))    

#Uloha 4
#zrealizujte rad (queue) pomocou jednosmerného spájaného zoznamu:
#pridávanie na koniec a uberanie zo začiatku
class Rad():
    class _Prvok():
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next;
    def __init__(self):
        self.zac = None
    def pridaj(self, data):
        if self.zac is None:
            self.zac = self._Prvok(data)
        else:
            pom = self.zac
            while pom.next is not None:
                pom = pom.next
            pom.next = self._Prvok(data)
    def vyber(self):
        if self.zac:
            pom = self.zac.data
            self.zac = self.zac.next
            return pom
    def daj_prvok(self):
        return self.zac.data
    def is_empty(self):
        if self.zac is None:
            return True
        return False    

#Uloha 5
#zmodifikujte algoritmus triedenia (2)
#aby pracoval s dvomi radmi (namiesto dvoch zásobníkov)
def utried2(pole):
    plni_sa = 2
    s1 = Rad()
    s2 = Rad()
    temp = []
    for prvok in pole:
        s1.pridaj(prvok)

    while True:
        
        if plni_sa == 1:
            utriedene = True
            prvok1 = s2.vyber()
            while not s2.is_empty():
                if prvok1 is None: break
                prvok2 = s2.vyber()

                if prvok1 > prvok2: utriedene = False
                if prvok1 < prvok2:
                    s1.pridaj(prvok1)
                    prvok1 = prvok2
                else:
                    s1.pridaj(prvok2)

            if prvok1 is None: break
            s1.pridaj(prvok1)
            if utriedene: break
            plni_sa = 2
            
        elif plni_sa == 2:
            utriedene = True;
            prvok1 = s1.vyber()
            while not s1.is_empty():
                prvok2 = s1.vyber()

                if prvok1 > prvok2: utriedene = False
                if prvok1 < prvok2:
                    s2.pridaj(prvok1)
                    prvok1 = prvok2
                else:
                    s2.pridaj(prvok2)
            if prvok1 is None: break
            s2.pridaj(prvok1)
            if utriedene: break
            plni_sa = 1
            
    if plni_sa == 2:
        while not s2.is_empty():
            temp.append(s2.vyber())
    else:
        while not s1.is_empty():
            temp.append(s1.vyber())
    return temp

def uloha5():
    import random, time
    print("Test jednoducheho pola")
    pole = [1,5,8,10,2]
    nove = utried2(pole)
    print(nove)
    print("Triedenie je sprave, pole1 == pole 2")
   
    print("Generujem pole...")
    velke_pole = []
    n = 100
    for i in range(n):
        velke_pole.append(random.randrange(10000))
    print("Triedim...")
    start = time.time()
    nvelke_pole1 = utried(velke_pole,"python")
    koniec1 = time.time()-start
    nvelke_pole2 = utried2(velke_pole)
    koniec2 = time.time()-start
    if nvelke_pole1 == nvelke_pole2:
        print("Triedenie je spravne, nvelke_pole1 == nvelke_pole2")
    print("Casy utriedenia {} prvkoveho pola:\nPython stack = {}\nSpajany zoznam (Queue)= {}".format(n,koniec1,koniec2))
    
