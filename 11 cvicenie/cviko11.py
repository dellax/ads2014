#uloha 1 
#trieda Trie z module trie.py je základom lexikografického stromu z
#prednášky 06lprednaska z prvého ročníka. V tejto triede sú naimplementované
#len metódy vloz() a __iter__().
#otestujte vložením aspoň 20 reťazcov a výpisom (pomocou __iter__() sa
#získajú všetky kľúče)
def uloha1():
    import trie
    strom = trie.Trie()
    pole = ["fdsfsdf","ijaoif asfjiasf ","dajiifj a ioasdjfa", "fandfn ajsf p"
            " oajsf ajfasf", " faioj fijasfa", " afiopj aisf asfpj,",
            "asfko akfaso f", " aosf asfkspaom "," asfjianjsf aofnaso fasiof"]
    for prvok in pole:
        strom.vloz(prvok, 0)
    for prvok in strom:
        print(prvok)
    print(len(pole))
    print(len(strom))

#uloha 2
#metóda vloz() je rekurzívna, pritom používa len chvostovú rekurziu
#prepíšte ju na nerekurzívnu funkciu

def uloha2():#test
    import trie
    strom = trie.Trie()
    pole = ["fdsfsdf","ijaoif asfjiasf ","dajiifj a ioasdjfa", "fandfn ajsf p"
            " oajsf ajfasf", " faioj fijasfa", " afiopj aisf asfpj,",
            "asfko akfaso f", " aosf asfkspaom "," asfjianjsf aofnaso fasiof"]
    for prvok in pole:
        strom.vloz(prvok, 0)
    for prvok in strom:
        print(prvok)
    print(len(pole))
    print(len(strom))
