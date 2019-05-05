import Heap as hp
import Node as nd
import Binary_tree as btree

if __name__ == "__main__":
    #file = open('test_case.txt')
    file = open('huffman.txt')
    lines = file.readlines()

    node_num = int(lines[0])    
    source = [int(i) for i in lines[1:]]

    hhp = hp.Heap(source, "min")
    min_node = hhp.get_top_value()
    bbt = btree.Binary_tree(hhp)

    cur_node = min_node
    counter = 0
    while cur_node.parent != None:
        cur_node = cur_node.parent
        counter +=1

    print("maximum length of a codeword is %i" %counter)
