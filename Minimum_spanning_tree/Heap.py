class Heap():
    def __init__(self, elements= list(), heap_type= 'min'):
        # data structure: [[vertices, keys]]
        self.elements = elements
        self.heap_type = heap_type
        pass

    def heap_update(self, new_elements):
        temp_id = len(self.elements)
        parent_id = temp_id//2
        self.elements.append(new_elements)
        self.heapify(parent_id, temp_id)
        return self

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
            self.elements[new_id] = self.elements[parent_id]
            self.elements[parent_id] = new_value
            grand_parent_id = parent_id//2  
            self.heapify(grand_parent_id, parent_id)
        return self

    def extract_value(self):
        value = self.elements.pop(0)[0]
        for i in range(len(self.elements)):
            heap = self.heapify(i//2, i)
        return [value, heap]

    def update_value():
        


    def __str__(self):
        return str(self.elements)