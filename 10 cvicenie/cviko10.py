#uloha 1 
#otestujte triedenie insert_sort():
#zistite, aké veľké náhodné polia sa utriedia približne za 1 sekundu a za
#2 sekundy
#vygenerujte dve rovnako veľké polia ako náhodné pole utriedené
#za 1 sekundu, ktoré sa budú triediť v najlepšom prípade (prvé) a
#v najhoršom prípade (druhé)

def insert_sort(pole):
    for i in range(1,len(pole)):
        prvok = pole[i]
        j = i - 1
        while j >= 0 and prvok < pole[j]:
            pole[j+1] = pole[j]
            j -= 1
        pole[j+1] = prvok
    return pole

def uloha1():
    import random, time
    pole = []
    cas1 = 0
    cas2 = 0
    najlepsi = 0
    najhorsi = 0
    n = 100
    while cas1 < 1:
        print("1/4, triedim {} prvkove pole ....". format(n))
        pole = []
        n += 100
        for i in range(n):
            pole.append(random.randrange(10000))
        start = time.time()
        p = insert_sort(pole)
        cas1 = time.time()-start
        print("1/4, utriedene za {}".format(cas1))

    n1 = n
    n = 100

    while cas2 < 2:
        print("2/4, triedim {} prvkove pole ....". format(n))
        pole = []
        n += 100
        for i in range(n):
            pole.append(random.randrange(10000))
        start = time.time()
        p = insert_sort(pole)
        cas2 = time.time()-start
        print("2/4, utriedene za {}".format(cas2))

    n2 = n
    n = 100

    while najlepsi < 1:
        print("3/4, triedim {} prvkove pole (najlepsi pripad) ....". format(n))
        pole = []
        n += 10000
        for i in range(n):
            pole.append(i)
        start = time.time()
        p = insert_sort(pole)
        najlepsi = time.time()-start
        print("3/4, utriedene za {}".format(najlepsi))

    n3 = n
    n = 100

    while najhorsi < 1:
        print("4/4, triedim {} prvkove pole (najhorsi pripad) ....". format(n))
        pole = []
        n += 100
        for i in range(n):
            pole.append(n-i)
        start = time.time()
        p = insert_sort(pole)
        najhorsi = time.time()-start
        print("4/4, utriedene za {}".format(najhorsi))

    n4 = n
    n = 100
        
    print("Za 1 sekundu insert_sort utriedi {} prvkove pole, cas = {}".format(n1, cas1))
    print("Za 2 sekundy insert_sort utriedi {} prvkove pole, cas = {}".format(n2, cas2))
    print("Za 1 sekundu insert_sort utriedi {} prvkove pole (najlepsi pripad), cas = {}".format(n3, najlepsi))
    print("Za 1 sekundu insert_sort utriedi {} prvkove pole (najhorsi pripad), cas = {}".format(n4, najhorsi))

#uloha 2
#spojazdnite testovanie merge_sort(), ktorý vygeneruje rekurzívne
#utriedené pole (funkcia nemení vstupné pole)
#zistite, aké veľké náhodné polia sa utriedia približne za 1 sekundu
#a za 2 sekundy
#porovnajte rýchlosť triedenia s insert_sort()
#triviálny prípad rekurzie je vtedy, keď je triedené pole prázdne
#alobo jednoprvkové, zmeňte ho tak, že ak je dĺžka poľa menšia ako
#napr. 32, tak sa toto pole utriedi insert_sortom, porovnajte rýchlosť
#takto upraveného triedenia s triedením s pôvodným merge_sortom

def merge_sort(pole):

    def merge(p1, p2):
        result,i1,i2 = [],0,0
        while i1 < len(p1) or i2 < len(p2):
            if i1 < len(p1) and (i2 == len(p2) or p1[i1] < p2[i2]):
                result.append(p1[i1])
                i1 += 1
            else:
                result.append(p2[i2])
                i2 += 1
        return result

    if len(pole) <= 1:
        return pole
    stred = len(pole)//2
    return merge(merge_sort(pole[:stred]),merge_sort(pole[stred:]))

def merge_sort2(pole):

    def merge(p1, p2):
        result,i1,i2 = [],0,0
        while i1 < len(p1) or i2 < len(p2):
            if i1 < len(p1) and (i2 == len(p2) or p1[i1] < p2[i2]):
                result.append(p1[i1])
                i1 += 1
            else:
                result.append(p2[i2])
                i2 += 1
        return result

    if len(pole) <= 32:
        return insert_sort(pole)
    stred = len(pole)//2
    return merge(merge_sort(pole[:stred]),merge_sort(pole[stred:]))

def uloha2():
    import time
    m1a, m1b, m1c1, m1c2, m2a, m2b, m2c1, m2c2 = 0, 0, 0, 0, 0, 0, 0, 0
    #merge1
    a = 100
    b = 100
    pole1 = []
    pole2 = []
    while True:
        pole1 = []
        for i in range(a):
            pole1.append(i)
        start = time.time()
        merge_sort(pole1)
        cas = time.time() - start
        if cas >= 2: break
        print("1", a, cas)
        a += 5000
    m1a = a
    m1c1 = cas
    print("Najlepsi pripad merge_sort1 = {} prvkove pole za {} sek".format(a, cas))
    while True:
        pole2 = []
        for i in range(b):
            pole2.append(b-i)
        start = time.time()
        merge_sort(pole2)
        cas = time.time() - start
        if cas >= 2: break
        print("2", b, cas)
        b += 5000
    print("Najhorsi pripad merge_sort1 = {} prvkove pole za {} sek".format(b, cas))
    m1b = b
    m1c2 = cas
    #merge 2
    a = 100
    b = 100
    pole1 = []
    pole2 = []
    while True:
        pole1 = []
        for i in range(a):
            pole1.append(i)
        start = time.time()
        merge_sort2(pole1)
        cas = time.time() - start
        if cas >= 2: break
        print("1", a, cas)
        a += 5000
    print("Najlepsi pripad merge_sort2 = {} prvkove pole za {} sek".format(a, cas))
    m2a = a
    m2c1 = cas
    while True:
        pole2 = []
        for i in range(b):
            pole2.append(b-i)
        start = time.time()
        merge_sort2(pole2)
        cas = time.time() - start
        if cas >= 2: break
        print("2", b, cas)
        b += 5000
    print("Najhorsi pripad merge_sort2 = {} prvkove pole za {} sek".format(b, cas))
    m2b = b
    m2c2 = cas
    print("Merge sort1:\nNajlepsi pripad: {} prvkov za {} sek\nNajhorsi pripad: {} prvkov za {} sek\nMerge sort2:\nNajlepsi pripad: {} prvkov za {} sek\nNajhorsi pripad: {} prvkov za {} sek\n".format(m1a, m1c1, m1b, m1c2, m2a, m2c1, m2b, m2c2))    
    
