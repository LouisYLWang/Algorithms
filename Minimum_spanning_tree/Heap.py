class Heap():
    def __init__(self, elements= list(), heap_type= 'min'):
        # ls to store the heap elements
        # data structure: [[index, keys]]
        self.elements = elements
        #heap_type: 'min'/'max'
        self.heap_type = heap_type
        # position of given index in elements ls
        self.restore_index()
        #self.index = [index for index,_ in enumerate(self.elements)] 
    
    # insert a [index, keys] into the heap and restore heap structure
    def insertion(self, new_elements):
        temp_id = len(self.elements)
        parent_id = temp_id//2
        self.elements.append(new_elements)
        self.index[new_elements[0]] = len(self.index)
        self.heapify(parent_id, temp_id)

    # get element's position in the heap by index 
    def get_position(self, index):
        return self.index[index]

    # set element's position in the heap by index 
    def set_position(self, index, value):
        self.index[index] = value

    def restore_index(self):
        self.index = {}
        for position, element in enumerate(self.elements):
            self.index[element[0]] = position

    # recursively restore heap invariant by swap
    def heapify(self, parent_id, new_id):
        flag = False
        if self.heap_type == 'min':
            if self.elements[parent_id][1] <= self.elements[new_id][1]:
                flag = True
        elif self.heap_type == 'max':
            if self.elements[parent_id][1] >= self.elements[new_id][1]:
                flag = True

        if flag:
            pass
        else:
            new_value = self.elements[new_id]

            #swap position in heap
            self.elements[new_id] = self.elements[parent_id]
            self.elements[parent_id] = new_value
 
            #bookeeping of swap position
            self.set_position(self.elements[new_id][0], new_id)
            self.set_position(self.elements[parent_id][0], parent_id)
            #self.index[self.elements[new_id][0]] = new_id
            #self.index[self.elements[parent_id][0]] = parent_id
            
            grand_parent_id = parent_id//2  
            self.heapify(grand_parent_id, parent_id)
        return self

    # extract min/max value of the heap
    def extract_value(self):
        value = self.elements.pop(0)[1]
        self.restore_index()
        #self.index[index] = None
        for i in range(len(self.elements)):
            self.heapify(i//2, i)
        return value

    # for heap: change the value by index
    # for minimal spanning tree: update node cost value by node label
    def update_value(self, index, value):
        self.elements[self.get_position(index)][1] = value
        for i in range(len(self.elements)):
            self.heapify(i//2, i)


    def __str__(self):
        return "elements: " +str(self.elements) + "\nindex: " +str(self.index)