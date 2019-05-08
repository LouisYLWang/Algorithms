file = open("mwis.txt")
lines = file.readlines()
nodes = [int(line) for line in lines[1:]]
node_num = int(lines[0])
subprob_cache = [0 for i in range(node_num)]

subprob_cache[1] = nodes[1]
res_set = set()

for i in range(2,node_num):
    subprob_cache[i] = max(subprob_cache[i-1],subprob_cache[i-2] + nodes[i])

#subprob_cache
i = node_num - 1

while i >=1:
    if subprob_cache[i-1] >= subprob_cache[i-2] + nodes[i]:
        i-=1
    else:
        res_set.add(nodes[i])
        i-=2

def check_in_set(index):
    return nodes[index-1] in res_set

list(map(check_in_set, [1, 2, 3, 4, 17, 117, 517, 997]))

for i in [1, 2, 3, 4, 17, 117, 517, 997]:
    print(nodes[i-1] in res_set)