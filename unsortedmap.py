from mapbase import *

class UnsortedMap(MapBase):
    def __init__(self):
        self.table = []

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError

    def __setitem__(self, key, value):
        for item in self.table:
            if key == item.key:
                item.value = value
                return
        self.table.append(self.Item(key, value))

    def __delitem__(self, key):
        for ix in range(len(self.table)):
            if key == self.table[ix].key:
                self.table.pop(ix)
                return
        raise KeyError

    def __len__(self):
        return len(self.table)

    def __iter__(self):
        for item in self.table:
            yield item.key
