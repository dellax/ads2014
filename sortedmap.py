from mapbase import *

class SortedMap(MapBase):

  def _find_index(self, key, low, high):     # vrati bud index, alebo kam vlozit
    if high < low:
      return high + 1
    else:
      mid = (low + high) // 2
      if key == self.table[mid].key:
        return mid
      elif key < self.table[mid].key:
        return self._find_index(key, low, mid - 1)
      else:
        return self._find_index(key, mid + 1, high)

  def __init__(self):
    self.table = []

  def __len__(self):
    return len(self.table)

  def __getitem__(self, k):
    j = self._find_index(k, 0, len(self.table) - 1)
    if j == len(self.table) or self.table[j].key != k:
      raise KeyError
    return self.table[j].value

  def __setitem__(self, k, v):
    j = self._find_index(k, 0, len(self.table) - 1)
    if j < len(self.table) and self.table[j].key == k:
      self.table[j].value = v
    else:
      self.table.insert(j, self.Item(k,v))

  def __delitem__(self, k):
    j = self._find_index(k, 0, len(self.table) - 1)
    if j == len(self.table) or self.table[j].key != k:
      raise KeyError
    self.table.pop(j)

  def __iter__(self):
    for item in self.table:
      yield item.key
