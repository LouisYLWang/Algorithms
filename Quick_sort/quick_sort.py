from random import randint
import numpy as np


data = np.loadtxt('QuickSort.txt')
data_list = data.tolist()
'''
QuickSort

Input: 
array A of n distinct integers, 
left and right endpoints l, r where l, r in {1,2,...,n} with l <= r. 

Post-condition:
elements of the subarray A[l],A [l + 1],...,A [r] are sorted from smallest to largest. 

'''
times= 0


def QuickSortQ1 (array, l, r):

    if l >= r:
        return array
    else:
        p = ChoosePivotQ1(array, l ,r) # pivot index
        array[p], array[l] = array[l], array[p]
        np = patrition(array, l, r)
        QuickSortQ1(array, l, np-1)
        QuickSortQ1(array, np+1, r)

def QuickSortQ2 (array, l, r):

    if l >= r:
        return array
    else:
        p = ChoosePivotQ2(array, l ,r) # pivot index
        array[p], array[l] = array[l], array[p]
        np = patrition(array, l, r)
        QuickSortQ2(array, l, np-1)
        QuickSortQ2(array, np+1, r)

def QuickSortQ3 (array, l, r):

    if l >= r:
        return array
    else:
        p = ChoosePivotQ3(array, l ,r) # pivot index
        array[p], array[l] = array[l], array[p]
        np = patrition(array, l, r)
        QuickSortQ3(array, l, np-1)
        QuickSortQ3(array, np+1, r)

'''
Partition 

Input: 
array A of n distinct integers, 
left and right endpoints l, r where l, r in {1,2,...,n} with l <= r. 
Postcondition: elements of the subarray A[l],A [l + 1],..., A [r] are partitioned around A[l]. 

Output: final position of pivot element.

'''

def patrition (array, l, r):
    global times
    pivot = array[l]
    i = l + 1
    for j in range(l+1, r+1):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[l], array[i-1] = array[i-1], array[l]
    #print(array)
    times += (r-l)
    return i-1

# Always use the ﬁrst element as the pivot。
def ChoosePivotQ1(array, l, r):
    return l

# Always use the last element as the pivot. 
def ChoosePivotQ2(array, l, r):
    return r

# Use the median-of-three as the pivot element, considers the ﬁrst, middle, and ﬁnal elements of the given array. It then identiﬁes which of these three elements is the median and returns this as the pivot
def ChoosePivotQ3(array, l, r):
    subarray = array[l:r]
    m = ((len(subarray)+1)//2)-1
    compare_list = sorted([array[l], array[r], subarray[m]])
    chosen_Index = array.index(compare_list[1])
    return chosen_Index

# Use a random element as the pivot. 
def ChoosePivot(array, l, r):
    pivotIndex = randint(l, r)
    print(pivotIndex)
    return pivotIndex



QuickSortQ1(data_list, 0, len(data_list)-1)
times = 0  # reset counter
QuickSortQ2(data_list, 0, len(data_list)-1)
times = 0  # reset counter
QuickSortQ3(data_list, 0, len(data_list)-1)

print(times)


#162085
#164123
#138382