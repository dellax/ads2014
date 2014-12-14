import tree_map

class AVLTreeMap(tree_map.TreeMap):

    #-------------------------- vnorena trieda Node --------------------------
    class Node(tree_map.TreeMap.Node):

        def __init__(self, key, value=None, parent=None):
            super().__init__(key, value, parent)
            self.height = 0            # este sa to prepocita

        def left_height(self):
            return self.left.height if self.left is not None else 0

        def right_height(self):
            return self.right.height if self.right is not None else 0

    #------------------------- pomocne metody -------------------------------
    def recompute_height(self, vrchol):
        vrchol.height = 1 + max(vrchol.left_height(), vrchol.right_height())

    def isbalanced(self, vrchol):
        return abs(vrchol.left_height() - vrchol.right_height()) <= 1

    def tall_child(self, vrchol, favorleft=False): 
        if vrchol.left_height() + (1 if favorleft else 0) > vrchol.right_height():
            return vrchol.left
        else:
            return vrchol.right

    def tall_grandchild(self, vrchol):
        child = self.tall_child(vrchol)
        alignment = (child == vrchol.left)
        return self.tall_child(child, alignment)

    def rebalance(self, vrchol):
        while vrchol is not None:
            old_height = vrchol.height                         
            if not self.isbalanced(vrchol):                      
                vrchol = self.restructure(self.tall_grandchild(vrchol))
                self.recompute_height(vrchol.left)
                self.recompute_height(vrchol.right)
            self.recompute_height(vrchol)                             
            if vrchol.height == old_height:                     
                vrchol = None                                    
            else:
                vrchol = vrchol.parent                    

  #--------------------- pomocne metody pre tree balancing ---------------------

    def relink(self, parent, child, make_left_child):
        if make_left_child:                           
            parent.left = child
        else:                                        
            parent.right = child
        if child is not None:                        
            child.parent = parent

    def rotate(self, vrchol):
        """Rotate vrchol p above its parent.

        Switches between these configurations, depending on whether p==a or p==b.

              b                  a
             / \                /  \
            a  t2             t0   b
           / \                     / \
          t0  t1                  t1  t2

        Caller should ensure that p is not the root.
        """
        """Rotate Position p above its parent."""
        x = vrchol
        y = x.parent                                 
        z = y.parent                                 
        if z is None:            
            self.root = x                              
            x.parent = None        
        else:
            self.relink(z, x, y == z.left)            

        if x == y.left:
            self.relink(y, x.right, True)             
            self.relink(x, y, False)                   
        else:
            self.relink(y, x.left, False)             
            self.relink(x, y, True)                    

    def restructure(self, x):
        """Perform a trinode restructure among Position x, its parent, and its grandparent.

        Return the Position that becomes root of the restructured subtree.

        Assumes the nodes are in one of the following configurations:

            z=a                 z=c           z=a               z=c  
           /  \                /  \          /  \              /  \  
          t0  y=b             y=b  t3       t0   y=c          y=a  t3 
             /  \            /  \               /  \         /  \     
            t1  x=c         x=a  t2            x=b  t3      t0   x=b    
               /  \        /  \               /  \              /  \    
              t2  t3      t0  t1             t1  t2            t1  t2   

        The subtree will be restructured so that the node with key b becomes its root.

                  b
                /   \
              a       c
             / \     / \
            t0  t1  t2  t3

        Caller should ensure that x has a grandparent.
        """
        """Perform trinode restructure of Position x with parent/grandparent."""
        y = x.parent
        z = y.parent
        if (x == y.right) == (y == z.right):  
            self.rotate(y)                                 
            return y                                        
        else:                                             
            self.rotate(x)                                      
            self.rotate(x)
            return x                                        

