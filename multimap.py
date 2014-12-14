class MultiMap:
  _MapType = dict                             # pouzity typ asociativne pole

  def __init__(self):
    self.asoc_pole = self._MapType()          # vytvori instanciu pre uchovavanie hodnot
    self._n = 0

  def __len__(self):
    return self._n

  def __iter__(self):
    for k,hodnoty in self.asoc_pole.items():
      for v in hodnoty:
        yield (k,v)

  def add(self, k, v):
    container = self.asoc_pole.setdefault(k, [])   # ak treba, vytvori prazdny zoznam
    container.append(v)
    self._n += 1

  def pop(self, k):
    hodnoty = self.asoc_pole[k]                    # moze vyvolat KeyError
    v = hodnoty.pop()
    if len(hodnoty) == 0:
      del self.asoc_pole[k]                        # uz nemame ziadne dvojice
    self._n -= 1
    return (k, v)

  def find(self, k):
    """vrati jednu z hodnot pre dany kluc"""
    hodnoty = self.asoc_pole[k]                    # moze vyvolat KeyError
    return (k, hodnoty[0])

  def find_all(self, k):
    """iteruje cez vestky s danym klucom"""
    hodnoty = self.asoc_pole.get(k, [])            # ak neexistuje hodnota, iteruje prazdny zoznam
    for v in hodnoty:
      yield (k,v)
