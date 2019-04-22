import sys
import Heap as hp

heap = hp.Heap([[0,float('inf')],[1,float('inf')],[2,float('inf')],[3,float('inf')]],'min')
#heap = hp.Heap([[1,16],[2,14],[3,10],[4,8],[5,7],[6,9],[7,3],[8,2],[9,4]],'min')
heap =  hp.Heap([[0,float('inf')]], 'min')
heap.extract_value()

print(heap.not_empty())
'''
print(heap)

heap.update_value(2, 3)
print(heap)

heap.insertion([5, 5])
print(heap)

heap.extract_value()
print(heap)

heap.extract_value()
print(heap)

'''
#heap2 = hp.Heap([[1,16],[2,14],[3,10],[4,8],[5,7],[6,9],[7,3],[8,2],[9,4]],'max')
#heap2.insertion([10,15])

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