from mapbase import *

class HashMap0(MapBase):
    def __init__(self, n=100):
        self.n = n
        self.table = [None] * n
        self.pocet = 0

    def __getitem__(self, key):
        if key < 0 or key >= self.n or self.table[key] is None:
            raise KeyError
        return self.table[key].value

    def __setitem__(self, key, value):
        if key < 0 or key >= self.n:
            raise KeyError
        if self.table[key] is None:
            self.pocet += 1
        self.table[key] = self.Item(key, value)

    def __delitem__(self, key):
        if key < 0 or key >= self.n or self.table[key] is None:
            raise KeyError
        self.table[key] = None
        self.pocet -= 1

    def __len__(self):
        return self.pocet

    def __iter__(self):
        for item in self.table:
            if item is not None:
                yield item.key
