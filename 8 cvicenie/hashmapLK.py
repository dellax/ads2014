from mapbase import *

class HashMap(MapBase):
    def __init__(self, n=10000):
        self.n = n
        self.table = [None] * n
        self.pocet = 0
        self.koliz = 0

##    def _hash(self, key):
##        h = 0
##        for znak in key:
##            h += ord(znak)
##            h -= h // 2
##            h += h % 2
##        return h

    def _find(self, key):
        ix = hash(key) % self.n
        volny = None
        while True:
            if self.table[ix] is None:
                if volny is None:
                    volny = ix
                return ix, volny
            # nastala kolizia
            self.koliz += 1
            if self.table[ix] is 'deleted':
                if volny is None:
                    volny = ix
            elif self.table[ix].key == key:
                return ix, volny
            ix = (ix+1) % self.n

    def __getitem__(self, key):
        ix,volny = self._find(key)

        if self.table[ix] is None:
            raise KeyError

        return self.table[ix].value

    def resize(self, nova):
        nove = [None] * nova
        i = 0
        for prvok in self.table:
            nove[i] = prvok
            i += 1
        self.table = nove
        self.n = i
                  
    def __setitem__(self, key, value):
        ix,volny = self._find(key)

        if self.table[ix] is not None:
            self.table[ix].value = value
        else:
            self.table[volny] = self.Item(key, value)
            self.pocet += 1
            # zväčšil sa počet prvkov, možno treba resize
            if self.pocet > self.n // 2:
                self.resize(self.n*2)

    def __delitem__(self, key):
        ix,volny = self._find(key)

        if self.table[ix] is None:
            raise KeyError

        self.table[ix] = 'deleted'
        self.pocet -= 1
        return

    def __len__(self):
        return self.pocet

    def __iter__(self):
        for item in self.table:
            if item is not None and item is not 'deleted':
                yield item.key
