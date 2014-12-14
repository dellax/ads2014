class MapBase:

    class _Item:

        def __init__(self, k, v):
            self._key = k
            self._value = v

    #------------------------- abstraktne metody -------------------------------------
    def __setitem__(self, key, value):
        raise KeyError

    def __delitem__(self, key):
        raise KeyError

    def __getitem__(self, key):
        raise KeyError

    def __len__(self):
        return 0

    def __iter__(self):
        while False:
            yield None

    #--------------------------------------------------------------
    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
        try:
            return self[key]
        except KeyError:
            return default

    def keys(self):
        "D.keys() -> a set-like object providing a view on D's keys"
        for key in self:
            yield key

    def items(self):
        "D.items() -> a set-like object providing a view on D's items"
        for key in self:
            yield (key, self[key])

    def values(self):
        "D.values() -> an object providing a view on D's values"
        for key in self:
            yield self[key]

    def __eq__(self, other):
        if not isinstance(other, MapBase):
            return NotImplemented
        return dict(self.items()) == dict(other.items())

    def __ne__(self, other):
        return not (self == other)

    def pop(self, key, default=object()):
        '''D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
          If key is not found, d is returned if given, otherwise KeyError is raised.
        '''
        try:
            value = self[key]
        except KeyError:
            if default is object():
                raise
            return default
        else:
            del self[key]
            return value

    def popitem(self):
        '''D.popitem() -> (k, v), remove and return some (key, value) pair
           as a 2-tuple; but raise KeyError if D is empty.
        '''
        try:
            key = next(iter(self))
        except StopIteration:
            raise KeyError
        value = self[key]
        del self[key]
        return key, value

    def clear(self):
        'D.clear() -> None.  Remove all items from D.'
        try:
            while True:
                self.popitem()
        except KeyError:
            pass

    def update(*args, **kwds):
        ''' D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
            If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
            If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
            In either case, this is followed by: for k, v in F.items(): D[k] = v
        '''
        if len(args) > 2:
            raise TypeError('update() takes at most 2 positional '
                            'arguments ({} given)'.format(len(args)))
        elif not args:
            raise TypeError('update() takes at least 1 argument (0 given)')
        self = args[0]
        other = args[1] if len(args) >= 2 else ()

        if isinstance(other, MapBase):
            for key in other:
                self[key] = other[key]
        elif hasattr(other, 'keys'):
            for key in other.keys():
                self[key] = other[key]
        else:
            for key, value in other:
                self[key] = value
        for key, value in kwds.items():
            self[key] = value

    def setdefault(self, key, default=None):
        'D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D'
        try:
            return self[key]
        except KeyError:
            self[key] = default
        return default

    def __repr__(self):
        res = ''
        for key in self:
            if res != '': res += ','
            res += '{!r}:{!r}'.format(key, self[key])
        return '{' + res + '}'
