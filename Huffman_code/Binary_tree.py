import Heap as hp
import Node as nd

class Binary_tree():

    def __init__(self, heap):
        
        while heap._len != 2:
            self.merge_subtree(heap)

        assert heap._len == 2
        self.root_node = self.merge_subtree(heap)

    def merge_subtree(self, heap):
        lf_node = heap.extract_value()
        rt_node = heap.extract_value()
        fa_node = nd.Node(val = lf_node.val + rt_node.val,
                          left = lf_node,
                          right = rt_node,
                          label = str(lf_node.val + rt_node.val)
                          )   # init father node
        lf_node.parent = rt_node.parent = fa_node
        heap.insertion(fa_node)
        return fa_node





