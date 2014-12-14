#uloha 2
#zo súboru text1.txt prečítajte anglický slovník (vyše 213 tisíc slov)
#a zistite, koľko kolízií vznikne pri použití štandardnej funkcie hash(),
#ak by sme mali k dispozícii pole:
#n je niekoľko miliónov
#n je dvojnásobok počtu slov
#n je dvojnásobok počtu slov zaokrúhlené nahor ale k najbližšiemu prvočíslu
#teda treba pre všetky slová zo slovníka zistiť ich hash() a zistiť
#koľkokrát sa niektorá z týchto hodnôt opakuje (hash(...) % n)
#pre každú z týchto podúloh, okrem celkového počtu kolízií, zistite
#aj maximálny počet slov, ktoré dodtávajú rovnaký index do tabuľky a
#tiež maximálnu dĺžku úseku v tabuľke, v ktorej nie je žiadna hodnota
#(počítajte s tým, že tabuľka je vlastne cyklické pole)
#úlohu otestujte aj so slovami v ďalších súboroch, napr. text3.txt a text4.txt

def uloha2():
    import hashmap
    poc = 0
    pole = []
    with open('text1.txt') as f:
        for slovo in f.read().split():
            poc += 1
            pole.append(slovo)
    a = hashmap.HashMap(10000000)
    b = hashmap.HashMap(poc)
    c = hashmap.HashMap(213623)
    for slovo in pole:
        a[slovo] = a.get(slovo, 0) + 1
        b[slovo] = b.get(slovo, 0) + 1
        c[slovo] = c.get(slovo, 0) + 1
    maxA = 0
    maxB = 0
    maxC = 0
    eA = 0
    eB = 0
    eC = 0
    maxeA = 0
    maxeB = 0
    maxeC = 0
    for prvok in a:
        if prvok is None:
            eA += 1
        else:
            if eA > maxeA:
                maxeA = eA
                eA = 0
        if len(prvok) > maxA:
            maxA = len(prvok)
    for prvok in b:
        if prvok is None:
            eB += 1
        else:
            if eB > maxeB:
                maxeB = eB
                eB = 0
        if len(prvok) > maxB:
            maxB = len(prvok)
    for prvok in c:
        if prvok is None:
            eC += 1
        else:
            if eC > maxeC:
                maxeC = eC
                eC = 0
        if len(prvok) > maxC:
            maxC = len(prvok)
        
    print("Pocet kolizii\na: {}\nb: {}\nc: {}".format(a.koliz, b.koliz, c.koliz))
    print("Maximalny pocet slov\na: {}\nb: {}\nc: {}".format(maxA, maxB, maxC))
    print("Maximalna dlzka prazdneho useku\na: {}\nb: {}\nc: {}".format(maxeA, maxeB, maxeC))

#uloha3
#navrhnite a naprogramujte vlastnú hešovaciu funkciu, ktorá dostane
#znakový reťazec a vyrobí z neho podľa možnosti jedinečné číslo
#využite funkciu ord()
#porovnajte s počtami kolízií z príkladu (2)

def uloha3():
    import hashmapN
    poc = 0
    pole = []
    with open('text1.txt') as f:
        for slovo in f.read().split():
            poc += 1
            pole.append(slovo)
    a = hashmapN.HashMap(10000000)
    b = hashmapN.HashMap(poc)
    c = hashmapN.HashMap(213623)
    for slovo in pole:
        a[slovo] = a.get(slovo, 0) + 1
        b[slovo] = b.get(slovo, 0) + 1
        c[slovo] = c.get(slovo, 0) + 1
    maxA = 0
    maxB = 0
    maxC = 0
    eA = 0
    eB = 0
    eC = 0
    maxeA = 0
    maxeB = 0
    maxeC = 0
    for prvok in a:
        if prvok is None:
            eA += 1
        else:
            if eA > maxeA:
                maxeA = eA
                eA = 0
        if len(prvok) > maxA:
            maxA = len(prvok)
    for prvok in b:
        if prvok is None:
            eB += 1
        else:
            if eB > maxeB:
                maxeB = eB
                eB = 0
        if len(prvok) > maxB:
            maxB = len(prvok)
    for prvok in c:
        if prvok is None:
            eC += 1
        else:
            if eC > maxeC:
                maxeC = eC
                eC = 0
        if len(prvok) > maxC:
            maxC = len(prvok)
        
    print("Pocet kolizii\na: {}\nb: {}\nc: {}".format(a.koliz, b.koliz, c.koliz))
    print("Maximalny pocet slov\na: {}\nb: {}\nc: {}".format(maxA, maxB, maxC))
    print("Maximalna dlzka prazdneho useku\na: {}\nb: {}\nc: {}".format(maxeA, maxeB, maxeC))

#uloha 4
#naprogramujte realizáciu pomocou verzia s ľubovoľným kľúčom a hľadaním miesta
#z prednášky (najprv riešte bez vyhadzovania prvku __delitem__)
#pri vkladaní (__setitem__), ak narazím na obsadené miesto v tabuľke hľadám
#najbližšie smerom k vyšším indexom (modulo veľkosť tabuľky) a na prvé voľné
#(t.j. None) zaradím
#pri hľadaní (__getitem__) kľúča, opäť prehľadávame aj susedné prvky, kým
#nenájdeme, resp. nenarazíme na None
#pri vyhadzovaní (__delitem__) je viac možností - najjednoduchšia je taká,
#že vyhadzovaný prvok sa nenahradí None ale nejakou inodu hodnotou, ktorá
#sa ľahko testuje a odlíši sa od normálnej dvojice (kľúč,hodnota)
#potom treba upraviť aj vkladanie (__setitem__) a hľadanie (__getitem__)
    
