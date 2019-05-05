class Node():
        
    def __init__(self,  val = 0, left = None, right = None, label = None ):
        # 0 => leaf, 1 => non-leaf 
        #self._type = _type

        # weight of the node for leaf node
        # weight of the subnodes for non-leaf node
        self.val = val

        # link to sub-nodes
        self.left = left
        self.right = right

        # label of the node
        self.label = label

    def __str__(self):
        return "%s:%s" %(str(self.label), str(self.val))