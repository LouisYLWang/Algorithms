from Disjoint_set import *
from copy import deepcopy
if __name__ == "__main__":
    file = open('clustering_big.txt')
    lines = file.readlines()

    [node_num, bits_num] = [int(i) for i in lines[0].split()]
    eles = [Element(i) for i in range(node_num)]
    clusters = [Disjoint_set(eles[i]) for i in range(node_num)]

    

    def ls_to_int(ls):
        return int(''.join(map(str, ls)))
    
    bits_hash = {}
    for i in range(node_num):
        key = ls_to_int(list(map(int, lines[i].split())))
        bits_hash[key]= i


    def get_hamdist_1(node):
        res = list()
        for i in range(bits_num):
            node_ = deepcopy(node)
            node_[i] = 1 - node_[i]
            res.append(node_)
        return list(map(ls_to_int, res))

    def get_hamdist_2(node):
        res = list()
        for i in range(bits_num):
            for j in range(i+1,bits_num):
                node_ = deepcopy(node)
                node_[i] = 1 - node_[i]
                node_[j] = 1 - node_[j]
                res.append(node_)
        return list(map(ls_to_int, res))

    for i in range(1,100000):
        node_str = list(map(int, lines[i].split()))
        target = get_hamdist_1(node_str) + get_hamdist_2(node_str)
        for j in target:
            if j in bits_hash:
                pass



    
    
    


