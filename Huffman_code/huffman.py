import Heap as hp
import Node as nd

file = open('test_case.txt')
lines = file.readlines()

node_num = int(lines[0])

source = [int(i) for i in lines[1:]]

print(hp.Heap(source, "min"))
