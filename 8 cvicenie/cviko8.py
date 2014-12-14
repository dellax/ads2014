#uloha1
#v poslednej prednáške 7. Asociatívne polia 2 nie je zrealizované automatické
#zväčšovanie poľa pri jeho zaplnení v triede HashMap. Doprogramujte:
#metódu resize(), ktorá zväčší asociatívne pole na zadanú veľkosť a
#pritom prekopíruje všetky kľúče na novú pozíciu
#do metódy __setitem__() dopíšte volanie resize() (ak je počet zapísaných
#dvojíc v poli väčší ako 50% kapacity poľa)
#do metódy _find() na správne miesto vložte počítanie kolízií a aj evidovanie
#najdlhšieho úseku hľadaného kľúča
def uloha1():
    import hashmapLK
    poc = 0
    pole = []
    with open('text1.txt') as f:
        for slovo in f.read().split():
            poc += 1
            pole.append(slovo)
    a = hashmapLK.HashMap(10000000)
    b = hashmapLK.HashMap(213622)
    c = hashmapLK.HashMap(213623)
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

#uloha 2
#metóda _find() v triede HashMap využíva štandardnú funkciu hash();
#predpokladajte, že kľúčom bude vždy iba znakový reťazec: nahraďte túto
#funkciu vlastnou verziou, v ktorej budete z ord() hodnôt počítať vlastnú
#hešovaciu funkciu
#k výslednej hodnote hešu postupne pripočítavajte kód znaku, pričom je
#vhodné tento súčet ešte zakaždým deliť nejakou hodnotou (a tiež aj
#spracovať zvyšok po delení)
#porovnajte s vytváraním frekvenčnej tabuľky v (1) príklade

# SPRAVENA V MODULE hashmapLK.py def _hash()


#uloha 3
#Zrealizujte základných 5 operácií dátového typu množina pomocou hešovacej
#tabuľky z (1) príkladu
#uvedomte si, že pri množinách nebudete potrebovať niektoré operácie z
#abstraktnej triedy MapBase (možno MapBase nebudete potrebovať vôbec)
#základné operácie pre množiny sú:
#S.add(e) - pridá nový prvok do množiny, ale len keď sa tam už nenachádzal
#S.discard(e) - ak sa prvok v množine nachádza, tak ho vyhodí (nehlási chybu)
#e in S - zistí, či sa prvok v množine nachádza
#len(S) - vráti počet prvkov množiny
#iter(S) - iteruje cez všetky prvky (v nejakom poradí)


#uloha 4
#pomocou vašej realizácie množiny naprogramujte vygenerovanie prvočísel
#metódou eratostenovho sita
    
