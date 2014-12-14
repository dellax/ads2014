import bin_tree, map_base

class TreeMap(bin_tree.BinTree, map_base.MapBase):
    
    def hladaj(self, vrchol, key):
        if key == vrchol.key:
            return vrchol                               # našiel
        elif key < vrchol.key and vrchol.left:
            return self.hladaj(vrchol.left, key)        # vnorenie do ľavého podstromu
        elif key > vrchol.key and vrchol.right:
            return self.hladaj(vrchol.right, key)       # vnorenie do pravého podstromu
        return vrchol

    def __getitem__(self, key):
        if self.is_empty():
            raise KeyError
        vrchol = self.hladaj(self.root, key)
        if key == vrchol.key:
            return vrchol.value if vrchol.value is not None else vrchol.key
        else:
            raise KeyError

    def __setitem__(self, key, value):
        if self.is_empty():
            self.add_root(key, value)
        else:
            vrchol = self.hladaj(self.root, key)
            if key == vrchol.key:
                vrchol.value = value                 # nastav novú asociovanú hodnotu
            elif key < vrchol.key:
                self.add_left(vrchol, key, value)    # zdedené z BinarnyStrom
            else:
                self.add_right(vrchol, key, value)   # zdedené z BinarnyStrom
            #### self.rebalance(vrchol)

    def __iter__(self):
        if not self.is_empty():
            for vrchol in self.inorder():
                yield vrchol.key

    def __delitem__(self, key):
        if self.is_empty():
            raise KeyError
        vrchol = self.hladaj(self.root, key)
        if key != vrchol.key:
            raise KeyError
        if vrchol.left and vrchol.right:                  # vrchol má oboch synov
            r = vrchol.left                               # hlada vrchol s maximálnou hodnotou
            while r.right:
                r = r.right
            vrchol.key = r.key
            vrchol.value = r.value
            vrchol = r                                    # nastavíme, že vyhadzovať budeme r
        # teraz má vrchol max. 1 syna
        self.delete(vrchol)                               # zdedené z BinarnyStrom
        #### self.rebalance(vrchol)

    def rebalance(self, vrchol): pass


