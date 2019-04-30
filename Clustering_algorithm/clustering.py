from Disjoint_set import *

def file_parser(file_name):
    file = open(file_name)
    lines = file.readlines()
    node_num = int(lines[0])
    edge_ls = list()
    edge_map = {}

    eles = [Element(i) for i in range(node_num)]
    clusters = [Disjoint_set(eles[i]) for i in range(node_num)]

    for line in lines[1:]:
        l_slices = line.split()
        start = int(l_slices[0])-1
        end = int(l_slices[1])-1
        length = int(l_slices[2])
        edge_ls.append(length)
        if length not in edge_map.keys():
            edge_map[length] = [[eles[start], eles[end]]]
        else:
            edge_map[length].append([eles[start], eles[end]])

    return  node_num, edge_ls, edge_map, eles, clusters

node_num, edge_ls, edge_map, eles, clusters = file_parser('clustering1.txt')

cluster_num  = 4
edge_ls.sort()
flag = len(clusters) 
while flag > cluster_num:
    curr_spacing = edge_ls.pop(0)
    for closest_pair in edge_map[curr_spacing]:
        p, q = closest_pair[0], closest_pair[1]
        if q.set != p.set:
            union(p.set, q.set)
            flag -= 1

print("final clusters are:")
for set_i in clusters:
    if not set_i.is_empty():
        print(set_i.get_elements())

print("maximum spacing of k = %d is:" %cluster_num)
while q.set == p.set:
    curr_spacing = edge_ls.pop(0)
    for closest_pair in edge_map[curr_spacing]:
        p, q = closest_pair[0], closest_pair[1]
else:
    print(curr_spacing)
    
