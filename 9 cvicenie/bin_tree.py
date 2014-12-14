class BinTree:
    class Node:
        def __init__(self, key, value=None, parent=None):
            self.key = key
            self.value = value
            self.parent = parent
            self.left = None
            self.right = None

        def __repr__(self):
            if self.value is not None:
                return '({!r},{!r})'.format(self.key, self.value)
            else:
                return repr(self.key)

    #------------------------------------------------------------------

    def __init__(self):
        self.root = None
        self.size = 0

    def add_root(self, key, value=None):
        if self.root:
            raise ValueError('koren existuje')
        self.size = 1
        self.root = self.Node(key, value)

    def add_left(self, vrchol, key, value=None):
        if vrchol.left:
            raise ValueError('lavy syn existuje')
        self.size += 1
        vrchol.left = self.Node(key, value, vrchol)

    def add_right(self, vrchol, key, value=None):
        if vrchol.right:
            raise ValueError('pravy syn existuje')
        self.size += 1
        vrchol.right = self.Node(key, value, vrchol)

    def delete(self, vrchol):
        '''vyhodi vrchol node a nahradi ho potomkom (ak ma prave jedneho)

        ValueError ak ma vrchol dvoch potomkov
        '''
        if vrchol.left and vrchol.right:
            raise ValueError('vrchol ma dvoch synov')
        syn = vrchol.left if vrchol.left else vrchol.right    # moze byt None
        if syn:
            syn.parent = vrchol.parent   # prepise sa potomkom
        if vrchol is self.root:
            self.root = syn              # moze sa stat rootom
        else:
            parent = vrchol.parent
            if vrchol is parent.left:
                parent.left = syn
            else:
                parent.right = syn
        self.size -= 1

    #------------------------------------------------------------------

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return len(self) == 0     # return self.root is None

    def __iter__(self):
        yield from self.inorder()

    def inorder(self, vrchol=None):
        if vrchol is None:
            if self.is_empty():
                return
            vrchol = self.root
        if vrchol.left:
            yield from self.inorder(vrchol.left)
        yield vrchol
        if vrchol.right:
            yield from self.inorder(vrchol.right)

    def children(self, vrchol):
        '''generuje iteraciu synov vrcholu'''
        if vrchol.left:
            yield vrchol.left
        if vrchol.right:
            yield vrchol.right

    def depth(self, vrchol):
        if vrchol == self.root:
            return 0
        else:
            return 1 + self.depth(vrchol.parent)

    def _height(self, vrchol):
        if vrchol.left is None and vrchol.right is None:
            return 0
        else:
            return 1 + max(self._height(syn) for syn in self.children(vrchol))

    def height(self, vrchol=None):
        if vrchol is None:
            vrchol = self.root
        return self._height(vrchol)

    def preorder(self, vrchol=None):
        if vrchol is None:
            if self.is_empty():
                return
            vrchol = self.root
        yield vrchol
        if vrchol.left:
            yield from self.preorder(vrchol.left)
        if vrchol.right:
            yield from self.preorder(vrchol.right)

    def postorder(self, vrchol=None):
        if vrchol is None:
            if self.is_empty():
                return
            vrchol = self.root
        if vrchol.left:
            yield from self.postorder(vrchol.left)
        if vrchol.right:
            yield from self.postorder(vrchol.right)
        yield vrchol

    def breadthfirst(self):
        '''generuje iteraciu vrcholov stromu algoritmom do sirky'''
        if not self.is_empty():
            front = [self.root]      # simuluje queue pomocou pola
            while front:
                vrchol = front.pop(0)       # draha operacia - zisiel by sa spajany zoznam
                yield vrchol
                for syn in self.children(vrchol):
                    front.append(syn)

    #-------------------- testovacie metody ---------------------------

    def add_random(self, key, value=None):
        if self.is_empty():
            self.add_root(key, value)
        else:
            vrchol = self.root
            while True:
                if random.randrange(2):
                    if vrchol.left:
                        vrchol = vrchol.left
                    else:
                        self.add_left(vrchol, key, value)
                        return
                else:
                    if vrchol.right:
                        vrchol = vrchol.right
                    else:
                        self.add_right(vrchol, key, value)
                        return

    sir = 800
    g = None
    
    def draw(self, vrchol=None, width=None, x=None, y=None):
        if self.g is None:
            import tkinter
            self.g = tkinter.Canvas(bg='white', width=self.sir, height=600)
            self.g.pack()
        elif vrchol is None:
            self.g.delete('all')
        if vrchol is None:
            self.g.delete('all')
            if self.is_empty():
                return
            vrchol = self.root
            if width is None: width = int(self.g['width'])//2
            if x is None: x = width
            if y is None: y = 30
        if vrchol.left:
            self.g.create_line(x, y, x - width//2, y + 50)
            self.draw(vrchol.left, width//2, x - width//2, y + 50)
        if vrchol.right:
            self.g.create_line(x, y, x + width//2, y + 50)
            self.draw(vrchol.right, width//2, x + width//2, y + 50)
        self.g.create_oval(x-15, y-15, x+15, y+15, fill='white')
        self.g.create_text(x, y, text=vrchol)
        if vrchol is self.root:
            self.g.update()
        
    #------------------------------------------------------------------

if __name__ == '__main__':
    import random

    strom = BinarnyStrom()
    for i in range(17):
        strom.add_random(random.randrange(100))

    print('preorder     =', list(strom.preorder()))
    print('inorder      =', list(strom.inorder()))
    print('postorder    =', list(strom.postorder()))
    print('breadthfirst =', list(strom.breadthfirst()))
    strom.draw()

    
