class Trie:    
    class Node:
        def __init__(self):
            self.value = None
            self.child = {}

        def __repr__(self):
            return 'Node(...)'

    #------------------------------------------------------------------

    def __init__(self):
        self.root = self.Node()

    def pridaj1(self, vrchol, key, value):
        if key == '':
            vrchol.value = value
        else:
            pismeno = key[0]
            if pismeno not in vrchol.child:
                vrchol.child[pismeno] = self.Node()
            self.pridaj1(vrchol.child[pismeno], key[1:], value)

    def vloz(self, key, value):
        self.pridaj1(self.root, key, value)

    def zisti(self, key):
        return None

    def zrus(self, key):
        ...


    #------------------------------------------------------------------

    def __len__(self):
        return 1
    
    def is_empty(self):
        return len(self) == 0
    
    def __iter__(self):
        return self.vypis(self.root, '')

    def vypis(self, vrchol, key):
        if vrchol is None:
            return
        if vrchol.value is not None:
            yield key
        for pismeno in vrchol.child:
            if vrchol.child[pismeno] is not None:
                yield from self.vypis(vrchol.child[pismeno], key+pismeno)


if __name__ == '__main__':
    tr = Trie()
    tr.vloz('abba', 1)
    tr.vloz('boom', 2)
    tr.vloz('bac', 3)


    
