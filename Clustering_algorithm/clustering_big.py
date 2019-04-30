from Disjoint_set import *

if __name__ == "__main__":
    file = open('clustering_big.txt')
    lines = file.readlines()
    node_num, bits_num = lines[0].split()
    eles = [Element(i) for i in range(node_num)]
    clusters = [Disjoint_set(eles[i]) for i in range(edge_num)]