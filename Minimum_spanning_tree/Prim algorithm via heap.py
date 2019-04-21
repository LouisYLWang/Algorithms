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


'''

print(heap_update([],5, "min"))
print(heap_update([5],6, "min"))
print(heap_update([5,6],2, "min"))
print(heap_update([16,14,10,8,7,9,3,2,4],15, "max"))
print(extract_value([4479, 4292, 4135, 1640, 1386, 2793, 2303, 625, 1260, 1354, 225],"max"))

heap = hp.Heap([[1,2],[2,3],[3,1],[4,6]],'min')
heap.heap_update([0,0])

heap2 = hp.Heap([[1,16],[2,14],[3,10],[4,8],[5,7],[6,9],[7,3],[8,2],[9,4]],'max')
heap2.heap_update([10,15])

'''
min = heap.extract_value()
print(min[0])
print(heap)