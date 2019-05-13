import numpy as np
#file_name = "knapsack1.txt"
file_name = "test_case1.txt"

file = open(file_name)
w_num, n_num  = map(int, file.readline().split())

A = np.zeros(shape = (w_num + 1, n_num + 1))


for n in range(1,n_num + 1):
    v_cur, w_cur = map(int, file.readline().split())
    #A[0:w_cur - 1, n] = 0
    for w_j in range(w_cur , w_num + 1):
            if w_j - w_cur >= 0 and w_j - w_cur <= w_num:
                A[w_j, n] = max(A[w_j - w_cur , n-1] + v_cur, A[w_j, n-1])
            else:
                A[w_j, n] = 0 
print(A[w_num, n_num])
print(A)