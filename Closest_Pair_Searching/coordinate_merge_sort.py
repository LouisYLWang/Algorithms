
''' coordinate MergeSort
Input: array A of n coordinate by [x,y].
Output: array with the same coordinates, sorted from smallest to largest based on either x or y.

ignoring base cases
C := recursively sort ﬁrst half of A
D := recursively sort second half of A
return Merge (C,D)
'''


def coordinate_merge_sort(array_b, coord = 'x'):
    b_len = len(array_b)
    cd_len = int(b_len//2)

    if b_len > 1:
        array_c = coordinate_merge_sort(array_b[:cd_len], coord)
        array_d = coordinate_merge_sort(array_b[cd_len:], coord)
        return merge(array_c, array_d, coord)
    else:
        return array_b         # did not consider this condition at first



'''Merge
Input: sorted arrays C and D (length n/2 each). 
Output: sorted array B (length n). 
Simplifying assumption: n is even.

 i := 1
 j := 1 
 for k := 1 to n do 
    if C[i] <D [j] then
        B[k] :=C[i]             // populate output array 
        i := i+1                // increment i 
    else                        // D[j] <C [i]
        B[k]:=D[j]
        j:=j+1
'''

def merge(array_c, array_d, coord):
    i = 0
    j = 0

    if coord == 'x':
        col = 0
    else:
        col = 1


    array_b = list()

    while i < len(array_c) and j < len(array_d):    # change to while loop since index k is low efficiency & meaningless
        if array_c[i][col] < array_d[j][col]:
            array_b.append(array_c[i])
            i += 1
        else:
            array_b.append(array_d[j])
            j += 1

    if i < j:
        array_b += array_c[i:]
    else:
        array_b += array_d[j:]

    return array_b

