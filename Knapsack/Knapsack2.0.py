import numpy as np
file_name = "knapsack1.txt"
#file_name = "test_case1.txt"

file = open(file_name)
[w_num, n_num]  = map(int, file.readline().split())

A = np.zeros(shape = (w_num + 1, 2))
for n in range(1,n_num + 1):
    [v_cur, w_cur] = map(int, file.readline().split())
    A[:, 0] = A[:,1]
    for w_j in range(w_cur , w_num + 1):
        if w_j < w_cur:
            A[w_j, 1] = A[w_j-1, 0]
        else:
            A[w_j, 1] = max(A[w_j - w_cur, 0] + v_cur, A[w_j, 0])
        #print(A)
print(A[w_num, 1])

