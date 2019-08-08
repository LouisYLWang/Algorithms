import matplotlib.pyplot as plt
import math
from scipy.special import comb
# dp_map:
# dim 0 (x axis): destination, indexing with 0 ... n
# dim 1 (y axis): subset, indexing with {0 ... n}
# adj_mat / adjacency matrix 
#
# def pre_processing():
#file = open('tsp.txt')
file = open('test_case_5.txt')
lines = file.readlines()
cities = [[]]
n = int(lines[0])
for l in lines[1:]:
    cities.append(list(map(float, l.split())))
adj_mat = [[None] * (n+1)  for i in range(n+1)]


x = [float(i[0]) for i in cities[1:]]
y = [float(i[1]) for i in cities[1:]]
plt.scatter(x, y)
plt.show()

for i in range(1, n+1):
    for j in range(1, n+1):
        if adj_mat[j][i]:
            adj_mat[j][i] = adj_mat[i][j]
        else:
            c1 = cities[i]
            c2 = cities[j]  
            adj_mat[j][i] = math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

#return adj_mat, dp_map

def get_bin(n, bits):
    if n == 0:
        return [0]
    res = list()
    digit = n-1
    cur = 1 << digit
    while cur < 1 << bits:
        for i in get_bin(n-1, digit):
            res.append(cur|i)
        digit += 1
        cur = 1 << digit
    return res

def get_sets(n):
    sets = dict()
    for i in range(1, n + 1):
        #print(i)
        sets[i] = get_bin(i, n)
    return sets

#sets: dict
#keys: subproblem size
#value: binary set

def get_ele(set_hash):
    set_hash >>= 1
    k = 2
    res = set()
    while set_hash:
        if set_hash & 1:
            res.add(k)
        k += 1
        set_hash >>= 1
    return res

#def TSP(n,adj_mat):

sets = get_sets(n)
A = {}
#deal with base case
for i in range(1<<n):
    if i & 1:
        A[i,1] = 0
    else: A[i,1] = float("inf")



for m in range(2, n+1):
    for subset in sets[m]:
        if subset & 1:
            print(bin(subset))
            elements = get_ele(subset)
            for j in elements:
                #print(subset, j)
                min_ = float("inf")
                for k in elements:
                    #print(k)
                    if k!= j:
                        if (subset ^ 1<<j-1,k) in A:
                            min_ = min(min_, A[subset ^ 1<<j-1, k] + adj_mat[k][j])
                A[subset,j] = min_

res = float("inf")
for j in range(2, n+1):
    res = min(res, A[(1<<n)-1, j] + adj_mat[j][1])
