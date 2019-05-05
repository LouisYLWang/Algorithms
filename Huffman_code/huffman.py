import Heap as hp
import Node as nd
import Binary_tree as btree

if __name__ == "__main__":
    #file = open('test_case.txt')
    file = open('huffman.txt')
    lines = file.readlines()

    node_num = int(lines[0])    
    source = [int(i) for i in lines[1:]]

    hp_min = hp.Heap(source, "min")
    hp_max = hp.Heap(source, "max")
    min_node = hp_min.get_top_value()
    max_node = hp_max.get_top_value()
    max_node = hp_min.unsorded_nodes[int(max_node.label)]

    bbt = btree.Binary_tree(hp_min)


    def get_result(flag):
        if flag == "min":
            cur_node = max_node
        if flag == "max":
            cur_node = min_node

        counter = 0
        while cur_node.parent != None:
            cur_node = cur_node.parent
            counter += 1

        print("%s length of a codeword is %i" %(flag, counter))

    
    get_result("max")
    get_result("min")
    