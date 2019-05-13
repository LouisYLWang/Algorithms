
file_name = "knapsack_big.txt"
file_name = "test_case3.txt"
file_name = "knapsack1.txt"


file = open(file_name)
w_num, n_num  = map(int, file.readline().split())
items = [[0,0]]

for line in file.readlines():
    v_cur, w_cur = map(int, line.split())
    items.append([v_cur, w_cur])

memory_hash = {}


def get_optimal_val(w_j, n):
    v_cur, w_cur = items[n]
    if n == 0: 
        return 0
    if (w_j, n) in memory_hash:
        return memory_hash[(w_j, n)]
    else:    
        if w_cur > w_j:
            res = get_optimal_val(w_j, n-1)

        else:
            res = max(get_optimal_val(w_j - w_cur, n-1) + v_cur, get_optimal_val(w_j, n-1) )
            
    memory_hash[(w_j, n)] = res
    return res

print(get_optimal_val(w_num, n_num))

