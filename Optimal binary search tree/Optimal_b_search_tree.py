import numpy as np
file_name = "input.txt"
lines = open(file_name).readlines()
nodes = list()
node_num = int(lines[0].split()[0])
for line in lines[1:]:
    nodes.append(float(line.split()[0]))

nodes = np.array(nodes)

A = np.diag(nodes)

for s in range(node_num):
    for i in range(node_num-s):
        min_val = node_num
        for j in range(s+1):
            r = i+j
            val = sum(nodes[i:i+s+1])
            if i <= r-1:
                val += A[i, r-1]
            if r+1 <= i+s:
                val += A[r+1, i+s]
            if val < min_val:
                min_val = val
        A[i,i+s] = min_val

print(A[0,node_num-1])

