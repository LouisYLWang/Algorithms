
'''  Counting Inversions
Input: An array A of distinct integers.
Output: The number of inversions of A—the number of pairs (i,j) of array indices with i<j and A[i] >A [j].

Sort-and-CountInv

Input: array A of n distinct integers.
Output: sorted array B with the same integers, and the number of inversions of A.

if n =0 or n =1 then // base cases
     return (A,0)
else (C,leftInv) :=Sort-and-CountInv(first half of A)
     (D,rightInv) := Sort-and-CountInv(second half of A)
     (B,splitInv) :=Merge-and-CountSplitInv(C,D)
     return (B,leftInv+ rightInv + splitInv)
'''


def sort_countInv(array_a):
    a_len = len(array_a)
    half_len = int(a_len//2)

    if a_len <= 1:
        return array_a, 0
    else:
        n_left = sort_countInv(array_a[:half_len])
        n_right = sort_countInv(array_a[half_len:])
        n_split = merge_countInv(n_left[0], n_right[0])
        return n_split[0], n_left[1] + n_right[1] + n_split[1]




''' Merge and count Inversion
Input: sorted arrays C and D (length n/2 each). 
Output: sorted array B (length n) and number of split inversion. 
Simplifying assumption: n is even.

 i := 1
 j := 1
 split_inversion := 0 
 for k := 1 to n do 
    if C[i] <D [j] then
        B[k] :=C[i]             // populate output array 
        i := i+1                // increment i 
    else                        // D[j] < C[i]
        B[k]:=D[j]
        j:=j+1
        split_inversion := split_inversion + (n/2 - i + 1)
    return (B, split_inversion) 
'''

def merge_countInv(array_c, array_d):
    i = 0
    j = 0
    splitInv = 0

    array_b = list()

    while i < len(array_c) and j < len(array_d):    # change to while loop since index k is low efficiency & meaningless
        if array_c[i] < array_d[j]:
            array_b.append(array_c[i])
            i += 1
            print(array_b, array_c, i, array_d, j, splitInv)
        else:
            array_b.append(array_d[j])
            j += 1
            splitInv += len(array_c) - i
            print(array_b, array_c, i, array_d, j, splitInv)

    if i < j:
        array_b += array_c[i:]
    else:
        array_b += array_d[j:]

    return array_b, splitInv



list_a = [1, 3, 5, 2, 4, 6]
list_b = [5, 4, 1, 8, 7, 2, 6, 3]
list_c = [12, 36, 83, 29, 14 ,92 ,43, 23, 0, 1, 23, 45, 390, 21]

print(sort_countInv(list_a))
print(sort_countInv(list_b))
print(sort_countInv(list_c))


