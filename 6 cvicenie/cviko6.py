# Uloha 1
# v prednáške sme ukázali heapsort zapísaný pomocou prioritného frontu s haldou
# triedenie haldou:
# def heap_sort(pole):
#     p = HeapPriorityQueue()
#     for i in pole:
#         p.add(i, i)
#     for i in range(len(pole)):
#         pole[i] = p.remove_min()[1]
# prepíšte túto funkciu tak, aby nepoužívala žiadne ďalšie štruktúry okrem
# pomocného poľa (typu list) pričom nepoužívajte žiadne pomocné funkcie - všetok
# kód bude len v tejto jedinej funkcii (obe rekurzívne funkcie prepíšete na while-cykly)
# váš algoritmus otestujte na správnosť a porovnajte na čas s pôvodným algoritmom,
# ktorý pracoval s HeapPriorityQueue

def heap_sort(pole):      
    p = []
    for i in pole:
        p.append(i)
        ix = len(pole) - 1
        parent = (ix-1)//2
        while ix > 0 and pole[ix] < pole[parent]:
            pole[ix], pole[parent] = pole[parent], pole[ix] # swap
            ix = parent
            parent = (ix-1)//2

    for i in len(pole):
        pole[0], pole[len(pole)-1] = pole[len(pole)-1], pole[0] # swap
        prvok = pole.pop()
        if 1 < len(p):
            if 2 < len(p):
                if pole[2] < pole[1]:
