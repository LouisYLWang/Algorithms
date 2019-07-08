import numpy as np


class Graph:
    def __init__(self, file_name):
        f = open(file_name, 'r')
        l1 = f.readline()
        n_v, n_e = map(int, l1.split())

        g = dict()
        g_rev = dict()
        for line in f.readlines():
            head_, tail_, len_ = map(int, line.split())
            if head_ not in g:
                g[head_] = dict()
            g[head_][tail_] = len_

            if tail_ not in g_rev:
                g_rev[tail_] = dict()
            g_rev[tail_][head_] = len_

        self.g = g
        self.n_v = n_v
        self.n_e = n_e
        self.g_rev = g_rev

    def floyd_warshall(self):
        # init i-j matrix
        res_mat = np.empty(shape=tuple([self.n_v + 1] * 3))
        res_mat[0] = np.ones((self.n_v + 1, self.n_v + 1)) * np.inf
        np.fill_diagonal(res_mat[0], 0)
        for i in self.g.keys():
            for j in self.g[i].keys():
                res_mat[0][i, j] = self.g[i][j]
        
        for k in range(1, g1.n_v + 1):
            for i in range(1, g1.n_v + 1):
                for j in range(1, g1.n_v+1):
                    res_mat[i,j,k] = min(res_mat[i,j,k-1], res_mat[i,k, k-1] + res_mat[k,j, k-1])
        return res_mat
    
    def bell_ford(self):
        self.g[0] = dict([(i, 0) for i in range(1,self.n_v + 1)])
        for i in self.g_rev.keys():
            self.g_rev[i][0] = 0
        cur_cache = dict([(i, 0) for i in range(0, self.n_v + 1)])

        for i in range(1, self.n_v + 1):
            pre_cache = cur_cache
            cur_cache = dict([(i, 0) for i in range(0, self.n_v + 1)])
            for v in range(1, self.n_v + 1):
                val1 = pre_cache[v]
                val2 = np.inf
                if v in self.g_rev:
                    for w in self.g_rev[v].keys():
                        if pre_cache[w] + self.g[w][v] < val2:
                            val2 = pre_cache[w] + self.g[w][v] 
                cur_cache[v] = min(val1, val2)
            
        if pre_cache != cur_cache:
            print("negative loop: NULL")
        else:
            node_weight = cur_cache
            for i in self.g.keys():
                for j in self.g[i].keys():
                    self.g[i][j] = self.g[i][j] + node_weight[i] - node_weight[j]
            return node_weight

        

