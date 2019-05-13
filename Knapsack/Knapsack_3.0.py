
file_name = "knapsack1.txt"
#file_name = "test_case2.txt"

file = open(file_name)
w_num, n_num  = map(int, file.readline().split())
items = [[0,0]]

for line in file.readlines():
    v_cur, w_cur = map(int, line.split())
    items.append([v_cur, w_cur])


def get_optimal_val(w_j, n):
    v_cur, w_cur = items[n]
    if n == 0 or w_cur > w_j:
        return 0
    else:
        #res = max(get_optimal_val(w_j - w_cur, n-1) + v_cur, get_optimal_val(w_j, n-1) )
        print("%i %i value is ？" %(w_j, n))
        return max(get_optimal_val(w_j - w_cur, n-1) + v_cur, get_optimal_val(w_j, n-1) )


get_optimal_val(w_num, n_num)

