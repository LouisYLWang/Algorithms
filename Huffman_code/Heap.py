import Node as nd

class Heap():
    def __init__(self, elements, heap_type = 'min'):
        # ls to store the heap nodes
        # data structure: [[index, keys]]
        self.nodes = list()
        self.unsorded_nodes = list()
        self._len = len(self.nodes)
        self.heap_type = heap_type
        for i, j in enumerate(elements):
            cur_node = nd.Node(val = j, label = str(i))
            self.insertion(cur_node)
            self.unsorded_nodes.append(cur_node)
        #heap_type: 'min'/'max'

        
    def insertion(self, new_node):
        temp_id = self._len
        parent_id = temp_id//2
        self.nodes.append(new_node)
        self.heapify(parent_id, temp_id)
        self._len += 1

    def not_empty(self):
        return self._len != 0

    # recursively restore heap invariant by swap
    def heapify(self, parent_id, new_id):
        flag = False
        if self.heap_type == 'min':
            if self.nodes[parent_id].val <= self.nodes[new_id].val:
                flag = True
        elif self.heap_type == 'max':
            if self.nodes[parent_id].val >= self.nodes[new_id].val:
                flag = True

        if flag:
            pass
        else:
            new_value = self.nodes[new_id]

            #swap position in heap
            self.nodes[new_id] = self.nodes[parent_id]
            self.nodes[parent_id] = new_value
            
            grand_parent_id = parent_id//2  
            self.heapify(grand_parent_id, parent_id)
        return self

    # extract min/max value of the heap
    def extract_value(self):
        return_value = self.nodes.pop(0)
        self._len -= 1 
        for i in range(len(self.nodes)):
            self.heapify(i//2, i)
        return return_value

    def get_top_value(self):
        return self.nodes[0]

    def __str__(self):
        return str([str(node) for node in self.nodes])