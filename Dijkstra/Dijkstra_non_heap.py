filename = "dijkstraData.txt"
#filename = "smalldataset.txt"
file=open(filename)
lines = file.readlines()
m = len(lines) # number of nodes

G = list()

for i in range(m):
    line_raw = lines[i].split()[1:]
    edge_dict = dict()
    for edge in line_raw:
        edge_end = int(edge.split(',')[0])
        edge_len = int(edge.split(',')[1])
        edge_dict[edge_end] = edge_len
    G.append(edge_dict)
file.close()

edge_list = [set(G[i].keys()) for i in range(m)]


X = set()
source_node = 1
X.add(source_node)
path_len = [1000000]*m
path_len[0] = 0

end_ver_list = list()
for i in edge_list:
    end_ver_list+=i

while set(end_ver_list) - X != set():
    i_ = 1
    j_ = 0
    min_weight = 10000
    for i in X:
        for j in edge_list[i-1]:
            if j in X:
                continue
            if path_len[i-1] + G[i-1][j] <= min_weight:
                min_weight = path_len[i-1] + G[i-1][j]
                i_ = i
                j_ = j
    print([i_,j_])
    print(min_weight)
    X.add(j_)
    path_len[j_-1] = min_weight
    print(path_len)


target = "7,37,59,82,99,115,133,165,188,197"
target_index = [int(i) for i in target.split(',')]

result = list()
for i in target_index:
    result.append(path_len[i-1])

print(result)



