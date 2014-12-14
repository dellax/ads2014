class MapBase:

    class Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value
        def __eq__(self, iny):
            return self.key == iny.key
        def __lt__(self, iny):
            return self.key < iny.key

    def __getitem__(self, key):
        raise KeyError

    def __setitem__(self, key, value):
        raise KeyError

    def __delitem__(self, key, value):
        raise KeyError

    def __len__(self):
        return 0

    def __iter__(self):
        while False:
            yield None

    #--------------------------------------

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
            

    def setdefault(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default
