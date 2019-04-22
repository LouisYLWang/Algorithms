import sys
import Heap as hp

file = open('edges.txt')
lines = file.readlines()

node_num = int(lines[0].split()[0])
edge_num = int(lines[0].split()[1])
print(node_num)

heap_ls = []
for i in range(node_num):
    heap_ls.append([i, float('inf')])

heap = hp.Heap(heap_ls, 'min')

