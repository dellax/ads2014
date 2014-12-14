#uloha 1
#vytvorte funkciu mocniny(n), ktorá
#vráti postupnosť (pole) druhých mocnín [1,4,9,16,...,n**2] vytvorenú
#pomocou for-cyklu a metódy append()
#vráti postupnosť (pole) ale vytvorené pomocou generovaného
#zápisu (napr. [... for i in ...])
#prerobte ju na generátorovú funkciu (použitím yield)
#prerobte ju na generátorovú funkciu (použitím generátorového
#zápisu (... for i in ...) bez yield)

def mocniny1(n):
    pole = []
    for i in range(n+1):
        pole.append(i**2)
    return pole

def mocniny2(n):
    return [i**2 for i in range(n+1)]

def mocniny3(n):
    for i in range(n+1):
        yield i**2

def mocniny4(n):
    return (i**2 for i in range(n+1))
    
def uloha1(n):
    print(mocniny1(n))
    print(mocniny2(n))
    for i in mocniny3(n):
        print(i, end = ' ')
    print()
    for i in mocniny4(n):
        print(i, end = ' ')
    print()

#uloha 2
#funkcia kopia(pole)
#vráti kópiu poľa (výsledok je typu list)
#prvky vráti ako postupnosť vygenerovanú generátorovou funkciou
#(použitím yield alebo yield from)
#otestujte, ako sa bude správať kopia(), ak jej parametrom je generátor
#namiesto poľa

def kopia(pole):
    yield from pole

def uloha2(n):
    pole = []
    for i in range(n):
        pole.append(n)
    k1 = kopia(pole)
    while True:
        try:
            print(next(k1))
        except:
            break
    y = yield from pole
    k2 = kopia(y)
    while True:
        try:
            print(next(k2))
        except:
            break 

#uloha 3
#funkcia map(funkcia, pole) vráti prvky poľa prerobené funkciou funkcia
#výsledok vytvorte najprv ako pole
#výsledok ako generátor
#otestujte, ako sa bude správať map(), ak druhým parametrom je generátor
#porovnajte so štandardnou funkciou map()

def map1(funkcia, pole):
    return [funkcia(prvok) for prvok in pole]

def map2(funkcia, pole):
    for prvok in pole:
        yield funkcia(prvok)

def uloha3():
    print(map(mocniny1, [1,2,3]))
    for prvok in map(mocniny1, [1,2,3]):
        print(prvok)
    print(map1(mocniny1, [1,2,3]))
    print(map2(mocniny1, [1,2,3]))
    for prvok in map2(mocniny1, [1,2,3]):
        print(prvok)

#uloha 4
#funkcia filter(funkcia, pole) vráti len tie prvky poľa,
#pre ktoré je splnená logická funkcia
#výsledok najprv ako pole
#výsledok ako generátor
#otestujte, ako sa bude správať filter(), ak druhým parametrom je generátor
#porovnajte so štandardnou funkciou filter()

def kladne(prvok):
    if prvok > 0: return True
    return False

def filter1(funkcia, pole):
    return [prvok for prvok in pole if funkcia(prvok)]

def filter2(funkcia, pole):
    for prvok in pole:
        if funkcia(prvok): yield prvok

def uloha4():
    pole = [-1,0,1,2,3]
    print(filter1(kladne,pole))
    print(filter1(kladne, pole))
    print(filter2(kladne, pole))
    a = filter2(kladne, pole)
    for i in a:
        print(i)

#uloha 5
#funkcia zdvoj(gen) vygeneruje každý prvok 2-krát za sebou
#vyskúšajte nielen s parametrom typu generátor,
#ale napr. aj so poleom alebo stringom

def zdvoj(gen):
    for prvok in gen:
        for i in range(2):
            yield prvok

def uloha5():
    pole = [1,2,3]
    s = "abc"
    a = zdvoj(pole)
    b = zdvoj(s)
    print(a, b)
    for prvok in a:
        print(next(a))
    for prvok in b:
        print(next(b))

#uloha 6
#funkcia spoj(gen1,gen2) vygeneruje najprv všetky prvky
#gen1 potom všetky prvky gen2
#vyskúšajte nielen s parametrami typu generátor,
#ale napr. aj s poliami a stringami
#porozmýšľajte nad verziou spoj(*gen), v ktorej sa spája
#ľubovoľne veľa generátorov

def spoj(gen1, gen2):
    for prvok in gen1:
        yield prvok
    for prvok in gen2:
        yield prvok

def spoj(*gen):
    for prvok in gen:
        for p in prvok:
            yield p

def uloha6():
    a = spoj("abc","def")
    while True:
        try:
            print(next(a))
        except:
            break

#uloha 7
#funkcia mix(gen1,gen2) generuje prvky na striedačku - ak v jednom skončí skôr,
#tak už len zvyšné druhého
#najprv s pomocným poľom (prvý generátor najprv presype prvky do poľa,
#a potom počas prechodu druhým generátorom dáva aj prvky z poľa)
#bez pomocného poľa len pomocou štandardnej funkcie next()
#porozmýšľajte nad verziou mix(*gen), v ktorej sa mixuje ľubovoľne
#veľa generátorov

def mix(gen1, gen2):
    for i in range(max(len(gen1), len(gen2))):
        try:
            yield gen1[i]
        except:
            pass
        try:
            yield gen2[i]
        except:
            pass

def mix(*gen):
    maxLen = 0
    for prvok in gen:
        if len(prvok) > maxLen:
            maxLen = len(prvok)
    for i in range(maxLen):
        for j in range(len(gen)):
            try:
                yield gen[j][i]
            except:
                pass
            
def uloha7():
    a = mix("abc", "defg")
    while True:
        try:
            print(next(a))
        except:
            break

#uloha 8
#pre triedu BinTree zrealizujte ďalšie metódy ako generátory
#metódy inorder() a breadthfirst() (do šírky) nech fungujú podobne ako
#napr. preorder() (ako generátor)

#class BinTree(Tree):

#    def inorder(self):
#        ...

#    def breadthfirst(self):
#        ...
#algoritmus “do šírky” generuje vrcholy po úrovniach: najpr. koreň,
#potom jeho synovia, potom jeho vnuci, ... (zrejme využijete queue), napr.

#algoritmus breadthfirst(T):
#    inicializuj queue Q s hodnotou T.root()
#    while Q not empty:
#        p = Q.dequeue()
#        spracuj vrchol p
#        for vrchol in T.children(p):
#            Q.enqueue(vrchol)
#obe metódy otestujte a porovnajte s výsledkami z preorder() a postorder()


#uloha 9
#zrealizujte triedu ArrayBinTree, v ktorej na reprezentáciu binárneho stromu
#využijete pole hodnôt:
#koreň je v nultom prvku pole[0]
#i-ty prvok (ak existuje) má svojich synov: ľavý v pole[2*i+1],
#pravý v pole[2*i+2]
#ak vrchol neexistuje, buď je jeho index >= len(pole), alebo jeho hodnota v poli je None
#naprogramujte všetky metódy:
#parameter vrchol v tejto reprezentácii označuje index do poľa
#ak nejaká metóda má vrátiť nejaký vrchol (teda index) a tento vrchol
#neexistuje, vráti None
#vašu implementáciu otestujte (mali by fungovať aj metódy preorder, postorder,
#inorder, height, depth)

class ArrayBinTree(BinTree):

    def __init__(self):
        ...

    def root(self):
        return ...

    def parent(self, vrchol):
        return ...

    def left(self, vrchol):
        return ...

    def right(self, vrchol):
        return ...

    def num_children(self, vrchol):
        yield ...

    def __len__(self):
        return ...

    def add_root(self, info):
        return ...

    def add_left(self, vrchol, info):
        return ...

    def add_right(self, vrchol, info):
        return ...

    def add_random(self, vrchol, info):
        ...


#uloha 10
#vieme, že zo samostatnej jednej vygenerovanej postupnosti vrcholov
#binárneho stromu (napr. preorder, inorder, ...) nevieme zrekonštruovať pôvodný
#strom. Navrhnite také textové výpisy stromu, z ktorých sá dá spätne
#vygenerovať pôvodný strom (predpokladáme, že hodnotami vo vrcholoch sú reťazce).
#Obe metódy dorobte do LinkedBinTree:
#metóda preorder_str() vytvorí reťazec, ktorý okrem hodnôt vo vrcholoch stromu
#obsahuje aj zátvorky ( a ) a hodnotu None na označenie neexistujúceho
#podstromu, napr. v tvare:

#('koreň',('ľavý',None,('11',None,None)),('pravý',('22',None,None),None))
#metóda directory() vytvorí viacriadkový reťazec (v každom riadku jeden vrchol), pričom každý vrchol je odsunutý v závislosti od svojej úrovne, napr. :

#koreň
#    ľavý

#        11
#    pravý
#        22
#zamyslite sa nad analogickou metódou directory(), ktorá by fungovala nie
#pre binárny strom ale pre všeobecný


#uloha 11
#do triedy LinkedBinTree pridajte metódy, ktoré z textu vygenerovaného
#metódami z (10) spätne vytvoria binárny strom:
#metóda create_from_preorder_str()
#metóda create_from_directory

#uloha 12
#napíšte metódu gener() pre binárny strom, ktorá prejde (vygeneruje)
#všetky prvky (v poradí preorder) ale bez rekurzie a zásobníka, napr.
#môžeme použiť “pravidlo pravej ruky”, keďže každý vrchol si eviduje aj
#svojho predka

    
    



