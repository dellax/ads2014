#uloha 1
#otestujte triedu TreeMap:
#je to realizácia utriedeného asociatívneho poľa pomocou binárneho
#vyhľadávacieho stromu
#zostrojte strom zo 100 náhodných hodnôt (napr. náhodné čísla od 0 do 1000)
#spojazdnite vykreslenie stromu (metóda draw()) a sledujte ako sa
#pridávajú, resp. vyhadzujú vrcholy

def uloha1():
    import tree_map, random, time
    strom = tree_map.TreeMap()
    for i in range(100):
        time.sleep(1)
        key = random.randrange(1000)
        strom[key] = strom.get(key, 0) + 1
        strom.draw()

#uloha 2
#pomocná metóda hladaj() v triede TreeMap je rekurzívna:
#v niektorých situáciách to spadne na preplnení rekurzie - vygenerujte
#také dáta, aby táto rekurzia spadla
#prepíšte túto metódu bez rekurzie a otestujte na dátach, na ktorých
#to predtým spadlo

def zhod_rekurziu():
    import tree_map
    strom = tree_map.TreeMap()
    for i in range(900): #max hlbka v py cca 900 padne ked bude range(1000)
        strom[i] = strom.get(i, 0) + 1
    strom.draw()

def uloha2():#upraveny modul tree_mapNR bez rekurzie
    import tree_mapNR
    strom = tree_mapNR.TreeMap()
    for i in range(1000): #max hlbka v py cca 900 padne ked bude range(1000)
        strom[i] = strom.get(i, 0) + 1
##    strom.draw() draw je stale rekurzivny


#uloha 3
#trieda AVLTreeMap by mala zabezpečiť vyvažovanie stromu
#spojazdnite túto verziu balancovaného BVS
#otestujte na náhodných údajoch
#vykresľujte strom do grafickej plochy aj s informáciami pre vyvažovanie
