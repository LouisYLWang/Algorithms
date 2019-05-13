import numpy as np
#file_name = "knapsack1.txt"
#file_name = "test_case1.txt"

file = open(file_name)
w_num, n_num  = map(int, file.readline().split())

A = np.zeros(shape = (w_num + 1, n_num + 1))

for n in range(1,n_num + 1):
    v_cur, w_cur = map(int, file.readline().split())
    #for debug use
    # print( v_cur, w_cur)
    for w_j in range(1, w_num + 1):
        if w_j < w_cur:
            A[w_j, n] = A[w_j, n-1]
        else:
            A[w_j, n] = max(A[w_j - w_cur , n-1] + v_cur, A[w_j, n-1])
        #for debug use
        # print("%i,%i : (1) = %i; (2) = %i; pick = %i" %(w_j, n, A[w_j - w_cur , n-1]+v_cur, A[w_j, n-1], A[w_j, n]))
print(A[w_num, n_num])
print(A)