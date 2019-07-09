from funcs import *
#g0 = Graph('toy_case.txt')
g1 = Graph('g1.txt')
g2 = Graph('g2.txt')
g3 = Graph('g3.txt')
g3.bell_ford()

#would out of memory
#g1.floyd_warshall()

'''
Thank to Abhijit Sarkar from cousera forum:
For the purposes of the assignment, it's not necessary to run Johnson's algorithm in it's entirely,
we can simply return the minimum value in the array returned by the Bellman-Ford algorithm. Let G'
be the modified graph after adding the vertex s s, d(u,v)≤0 ∀(u,v)∈ G′. Since s is directly connected
to both u and v, if there's an existing path p between u and v in G' s.t. length(p)>0, it is not the
shortest path found by BF algorithm. In other words, running BF algorithm on the modified graph upper 
bounds all shortest path lengths by zero, while preserving the negative path lengths.
'''

