#uloha 1
#Zapíšte nerekurzívnu aj dve rekurzívne verzie funkcie,
#ktorá počíta súčet prvkov poľa
#2 verzie rekurzívnej funkcie:
#v prvej sa pripočíta prvý prvok poľa k súčtu zvyšných prvkov
#v druhej sa vypočíta súčet prvkov v prvej polovici poľa a pripočíta sa súčet
#všetkých prvkov v druhej polovici
#odhadnite zložitosť všetkých troch verzií
#porovnajte rýchlosť behu jednotlivých verzií pre veľké náhodne
#vygenerované pole

def nerekurz_funct(pole):
    suc = 0
    for prvok in pole:
        suc += prvok
    return suc

def rekurz_funct1(pole):
    if len(pole) == 0: return 0
    return pole[0] + rekurz_funct1(pole[1:])

def rekurz_funct2(pole):
    if len(pole) == 0: return 0
    if len(pole) == 1: return pole[0]
    return rekurz_funct2(pole[:len(pole)//2]) + rekurz_funct2(pole[len(pole)//2:])

def uloha1():
    import random, time
    n = 100000
    pole = []
    for i in range(n):
        pole.append(random.randrange(10000))
    start = time.time()
    s1 = nerekurz_funct(pole)
    cas1 = time.time() - start

##    start = time.time()
##    s2 = rekurz_funct1(pole)
##    cas2 = time.time() - start
    s2 = "ndef"
    cas2 = "ndef"
    
    start = time.time()
    s3 = rekurz_funct2(pole)
    cas3 = time.time() - start

    print("Nerekurzivna f: suc = {}, cas = {}\nRekurzia1: suc = {}, cas = {}\nRekurzia2: suc = {}, cas = {}\n".format(s1,cas1,s2,cas2,s3,cas3))

#uloha 2
#zapíšte verzie funkcie, ktorá počíta i-ty člen fibonacciho
#postupnosti (0,1,1,2,3,5,8,13,...):
#nerekurzívne pomocou cyklu
#rekurzívna funkcia, ktorá rekurzívne volá samu seba pre (i-1) aj pre (i-2) prvok
#odhadnite zložitosť oboch verzií, odmerajte beh pre veľké n (nech test zostaví
#pole prvých n-fibonacciho čísel)
#môže vám pomôcť, keď okrem výpočtu fibonacciho čísla bude funkcia vracať aj
#počet rekurzívnych volaní (resp. bude tento počet počítať v nejakej globálnej
#premennej)
def nerekurz_fib(n):
    n1 = 0
    n2 = 0
    if (n <= 1): return 1
    n1 = n2 = 1
    for i in range(3, n+1):
        pom = n2
        n2 += n1
        n1 = pom
    return n2 + n1

poc_fib = 0
def rekurz_fib(n):
    global poc_fib
    poc_fib += 1  
    if (n <= 1): return 1
    return rekurz_fib(n-1) + rekurz_fib(n-2)

def uloha2(n):
    global poc_fib
    import time
    start = time.time()
    for i in range(n):
        poc_fib = 0
        print("Rekurzivna fib n = {}, hodnota = {}, cas = {}, pocetRek = {}".format(i, rekurz_fib(i), time.time()-start, poc_fib))
        start = time.time()
        print("Nerekurzivna fib n = {}, hodnota = {}, cas = {}".format(i, nerekurz_fib(i), time.time()-start))

#uloha 3
#zapíšte takúto rekurzívnu verziu výpočtu fibonacciho čísel (tzv. memoizácia):
#funkcia si bude súkromne udržiavať pomocné pole (list alebo dict),
#ktoré je na začiatku prázdne
#pri každom volaní sa funkcia najprv pozrie do poľa, či takúto hodnotu už
#niekedy v minulosti nepočítala a ak áno, tak len vráti už pred tým počítaný
#výsledok
#ak sa takáto hodnota ešte nepočítala, tak sa klasicky (rekurzívne) vypočíta a
#tesne pred návratom (return) si túto hodnotu do pomocného poľa odloží
#odmerajte čas výpočtu prvých n fibonacciho čísel

mem = dict()
def fib(n):
    if n in mem: return mem[n]
    if n <= 1: vys = 1
    else: vys = fib(n-1) + fib(n-2)
    mem[n] = vys
    return vys 

def uloha3(n):
    import time
    for i in range(n):
        start = time.time()
        print("n = {}, hodnota = {}, cas = {}".format(i, fib(i), time.time()-start))

#uloha 4
#zapíšte funkciu, ktorá zisťuje, či sú všetky prvky poľa navzájom rôzne
#(funkcia vráti True alebo False):
#rôzne verzie funkcie:

def zisti1(pole):
    for i in range(len(pole)):
        for j in range(len(pole)):
            if pole[i] == pole[j] and i != j: return False
    return True

def zisti2(pole):
    ...

def uloha4():
    ...

#uloha 5
#zapíšte rekurzívnu verziu funkcie, ktorá počíta k-tu mocninu čísla n,
#pričom využije takúto vlastnosť celočíslených mocnín:
#mocnina(n, 2k) == mocnina(n, k)**2 pre párne k
#mocnina(n, 2k+1) == n * mocnina(n, k)**2 pre nepárne k
#zistite, koľko je v tomto algoritme násobení a koľko rekurzívnych volaní

poc_rek = 0
poc_nas = 0
def mocnina(n, k):
    global poc_nas
    global poc_rek
    poc_rek += 1
    if k == 0: return 1
    if k == 1: return n
    if k % 2 == 0:
        poc_nas += 1
        return mocnina(n, k/2) * mocnina(n, k/2)
    if k % 2 != 0:
        poc_nas += 2
        return n * mocnina(n, (k-1)/2) * mocnina(n, (k-1)/2)

def uloha5(n, k):
    global poc_nas
    global poc_rek
    poc_nas = 0
    poc_rek = 0
    print("n^k = {}, poc_nas = {}, poc_rek = {}".format(mocnina(n, k), poc_nas, poc_rek))

#uloha 6 DOKONCIT
#zapíšte a porovnajte na rýchlosť dve verzie quick-sortu, pričom
#obe verzie nevracajú žiadnu hodnotu (t.j. vracajú None) ale len
#modifikujú skutočný parameter pole:
#pre prvú verziu využite http://python2013.input.sk/07lprednaska

def quick_sort(pole):
    def rozdel(z,k):
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

##def quick_sort2(pole):
##    pom = []
##    if len(pole) <= 1:
##        
##    pivot, mensie, vacsie = None, [], []
##    for prvok in pole:
##        if pivot is None:
##            pivot = prvok
##        elif prvok < pivot:
##            mensie.append(prvok)
##        else:
##            vacsie.append(prvok)
##    pole = quick_sort2(mensie) + [pivot] + quick_sort2(vacsie)

def uloha6(n):
    import random, time
    pole1 = []
    pole2 = []
    for i in range(n):
        prvok = random.randrange(10000)
        pole1.append(prvok)
        pole2.append(prvok)
    start = time.time()
    quick_sort(pole1)
    cas1 = time.time() - start

    start = time.time()
    quick_sort2(pole2)
    cas2 = time.time() - start
    
    print(pole1)
    print(pole2)
    print("Pre n = {}:\nQsort1 = {}\nQsort2 = {}\nZhoda triedenia = {}".format(n, cas1, cas2, pole1 == pole2))


#uloha 7 DOKONCIT
#zapíšte rekurzívnu funkciu, ktorá vráti pole všetkých podmožín zadanej množiny
def Pa(mnoz, k = 0):
    def p(m, k):
        pom = []
        if k == 0:
            return {}
        if len(m) == k:
            return (set(m))
        pom.extend([m[:k-1]+[i] for i in a[k-1:]])
        for prvok in pom:
            prvok = set(prvok)
        return pom + p(m[1:],k)
    pole = []
    pole += p(list(mnoz), k)
    k += 1
    
    

b = []
def abc(a,k):
    if len(a)==k:
        b.append(a)
        return b

    b.extend([a[:k-1]+[i] for i in a[k-1:]])    
    return abc(a[1:],k)


#print (abc([1,2,3,4,5],3))
print(Pa({1,2,3}))

