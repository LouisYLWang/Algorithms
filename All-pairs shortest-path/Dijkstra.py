#g1 = Graph('toy_case.txt')
g1 = Graph('g3.txt')
g1.bell_ford()
g1.g



#Dijkstra 
G = g1.g
m = g1.n_v
edge_list = dict()
for i in G.keys():
    edge_list[i] = set(G[i].keys())

X = set()
source_node = 1
X.add(source_node)
path_len = [np.inf]* (m+1)
path_len[1] = 0

end_ver_list = list()
for i in edge_list:
    end_ver_list += edge_list[i]

while set(end_ver_list) - X != set():
    i_ = 1
    j_ = 0
    min_weight = np.inf
    for i in X:
        if i in edge_list:
            for j in edge_list[i]:
                if j in X:
                    continue
                if path_len[i] + G[i][j] <= min_weight:
                    min_weight = path_len[i] + G[i][j]
                    i_ = i
                    j_ = j
    #print([i_,j_])
    #print(min_weight)
    X.add(j_)
    path_len[j_] = min_weight
    #print(path_len)
path_len
#path_len[1] + G[1][2] <= min_weight
