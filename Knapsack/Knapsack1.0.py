import numpy as np
file_name = "knapsack1.txt"
file = open(file_name)
[w_num, n_num]  = map(int, file.readline().split())

A = np.zeros(shape = (w_num + 1, n_num + 1))


for n in range(1,n_num + 2):
    [v_cur, w_cur] = map(int, file.readline().split())
    print(v_cur, w_cur) 
    A[0:w_cur, n] = 0
    for w_j in range(w_cur + 1, w_num + 2):
        A[w_j, n] = max(A[w_j - w_cur, n-1] + n, A[w_j, n-1])
                
