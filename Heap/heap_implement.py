def heap_update(heap, new_node, heap_type):
    heapsize = len(heap)
    temp_id = heapsize
    parent_id = temp_id//2
    heap.append(new_node)
    heapify(parent_id, temp_id, heap, heap_type)
    return heap

def heapify(parent_id, new_id, heap, heap_type):
    if heap_type == 'min':
        if heap[parent_id] <= heap[new_id]:
            pass
        else: 
            new_value = heap[new_id]
            heap[new_id] = heap[parent_id]
            heap[parent_id] = new_value
            grand_parent_id = parent_id//2  
            heapify(grand_parent_id, parent_id, heap, heap_type)

    if heap_type == 'max':
        if heap[parent_id] >= heap[new_id]:
            pass
        else: 
            new_value = heap[new_id]
            heap[new_id] = heap[parent_id]
            heap[parent_id] = new_value
            grand_parent_id = parent_id//2  
            heapify(grand_parent_id, parent_id, heap, heap_type)
    return heap

def extract_value(heap, value_type):
    value = heap.pop(0)
    for i in range(len(heap)):
        heap = heapify(i//2, i,heap, value_type)
    return [value, heap]
    


'''
test

print(heap_update([4,4,8,9,4,12,9,11,13,7,10],5, "min"))
print(heap_update([16,14,10,8,7,9,3,2,4],15, "max"))
print(extract_value([4479, 4292, 4135, 1640, 1386, 2793, 2303, 625, 1260, 1354, 225],"max"))
'''


if __name__ == '__main__':
    file = open("Median.txt")
    lines = file.readlines()
    max_heap = []
    min_heap = [int(lines[0])]
    median_ls = [int(lines[0])]

    for line in lines[1:]:
        new_node = int(line)
        if new_node <= min_heap[0]:
            max_heap = heap_update(max_heap, new_node, "max")
        else:
            min_heap = heap_update(min_heap, new_node, "min")
  
        if len(min_heap)-len(max_heap) > 1:
            shift_node, min_heap = extract_value(min_heap, 'min')
            heap_update(max_heap, shift_node, "max")
        elif len(max_heap)-len(min_heap) > 1:
            shift_node, max_heap = extract_value(max_heap, 'max')
            heap_update(min_heap, shift_node, "min")

        if len(max_heap)==len(min_heap):
            median_ls.append(max_heap[0])
        elif len(max_heap)-len(min_heap) == 1:
            median_ls.append(max_heap[0])
        elif len(min_heap)-len(max_heap) == 1:
            median_ls.append(min_heap[0])

    

#print(median_ls)
print(sum(median_ls)%10000)



   

