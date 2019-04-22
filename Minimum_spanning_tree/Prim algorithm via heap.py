import sys
import Heap as hp

file = open('edges.txt')
lines = file.readlines()

node_num = int(lines[0].split()[0])
ver_num = int(lines[0].split()[1]) * 2

ajacent_ls = [[] for i in range(node_num)]

for line in lines[1:]:
    start = int(line.split()[0]) - 1
    end = int(line.split()[1]) - 1
    cost = int(line.split()[2])
    ajacent_ls[start].append([end,cost])
    ajacent_ls[end].append([start,cost])
    

heap_ls = []
for i in range(node_num):
    heap_ls.append([i, float('inf')])

heap = hp.Heap(heap_ls, 'min')
heap.update_value(0, 0)


res = 0
while len(heap.index) > 0 :
    extract_value = heap.extract_value()
    u = extract_value[0]
    res += extract_value[1]
    for i in ajacent_ls[u]:
        index = i[0]
        cost = i[1]
        if index in heap.index and cost < heap.elements[heap.get_position(index)][1]:
            heap.update_value(index, cost)
    
    #for debugging
    # print([i[1] for i in heap.elements])
    #print(heap.index)

print(res)
