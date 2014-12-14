from mapbase import *

class HashMap(MapBase):
    def __init__(self, n=1000000):
        self.n = n
        self.table = [None] * n
        self.pocet = 0
        self.koliz = 0

    def _hash(self, key):
        h = 0
        for znak in key:
            h += ord(znak)
        return h

    def __getitem__(self, key):
        ix = self._hash(key) % self.n

        if self.table[ix] is None:
            raise KeyError

        for item in self.table[ix]:
            if key == item.key:
                return item.value
        raise KeyError

    def __setitem__(self, key, value):
        ix = self._hash(key) % self.n

        if self.table[ix] is None:
            self.table[ix] = [self.Item(key, value)]
        else:                                            # kolizia
            for item in self.table[ix]:
                if key == item.key:
                    item.value = value
                    return
            self.table[ix].append(self.Item(key, value))
            self.koliz += 1
        self.pocet += 1

    def __delitem__(self, key):
        ih = self._hash(key) % self.n

        if self.table[ih] is None:
            raise KeyError

        for ix in range(len(self.table[ih])):
            if key == self.table[ih][ix].key:
                self.table[ih].pop(ix)
                self.pocet -= 1
                return
        raise KeyError

    def __len__(self):
        return self.pocet

    def __iter__(self):
        for tab in self.table:
            if tab is not None:
                for item in tab:
                    yield item.key
