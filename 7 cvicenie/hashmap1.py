from mapbase import *

class HashMap1(MapBase):
    def __init__(self, n=1000):
        self.n = n
        self.table = [None] * n
        self.pocet = 0

    def __getitem__(self, key):
        if self.table[key%self.n] is None:
            raise KeyError

        for item in self.table[key%self.n]:
            if item.key == key:
                return item.value
        raise KeyError

    def __setitem__(self, key, value):
        if self.table[key%self.n] is None:
            self.pocet += 1
            self.table[key%self.n] = [self.Item(key, value)]
            return
        #kolizia
        for item in self.table[key%self.n]:
            if item.key == key:
                item.value = value
                return
        self.table[key%self.n].append(self.Item(key, value))

    def __delitem__(self, key):
        if self.table[key%self.n] is None:
            raise KeyError

        self.table[key%self.n] = None
        self.pocet -= 1

    def __len__(self):
        return self.pocet

    def __iter__(self):
        for pole in self.table:
            if pole is not None:
                for item in pole:
                    yield item.key
