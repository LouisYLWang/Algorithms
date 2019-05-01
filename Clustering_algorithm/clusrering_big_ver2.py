from Disjoint_set import *
from copy import deepcopy

#if __name__ == "__main__":
file = open('clustering_big.txt')
lines = file.readlines()

[node_num, bits_num] = [int(i) for i in lines[0].split()]
eles = [Element(i) for i in range(1, node_num)]
clusters = [Disjoint_set(ele) for ele in eles]

def ls_to_str(ls):
    return ''.join(map(str, ls))
    
bits_hash = {}
for i in range(node_num):
    key = ls_to_str(list(map(int, lines[i+1].split())))
    bits_hash[key]= i+1


def get_hamdist_1(node):
    res = list()
    for i in range(bits_num):
        node_ = deepcopy(node)
        node_[i] = 1 - node_[i]
        res.append(node_)
    return list(map(ls_to_str, res))

def get_hamdist_2(node):
    res = list()
    for i in range(bits_num):
        for j in range(i+1,bits_num):
            node_ = deepcopy(node)
            node_[i] = 1 - node_[i]
            node_[j] = 1 - node_[j]
            res.append(node_)
    return list(map(ls_to_str, res))

set_num = node_num

for i in range(1,200001):
    node_str = list(map(int, lines[i].split()))
    target = get_hamdist_1(node_str) + get_hamdist_2(node_str)
    for j in target:
        if j in bits_hash:
            node_1 = eles[i-1]
            node_2 = eles[bits_hash[j]-1]
            set_1 = node_1.set
            set_2 = node_2.set

            #print("node 1: %s \nnode 2: %s" % (node_1, node_2))
            if  set_1 != set_2:
                    union(set_1, set_2)
                    set_num -= 1

print(set_num)


