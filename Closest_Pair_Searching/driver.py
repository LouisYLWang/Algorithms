from coordinate_merge_sort import coordinate_merge_sort
from closest_pair_searching import *
import numpy as np


points = [[1,2],[3,4],[5,6],[4,8],[5,9],[2,2],[4,3],[4,1],[8,2],[2,8],[9,1],[2,6],[1,9],[2,1],[1,6],[0,8]]

p_x = coordinate_merge_sort(points, 'x')
p_y = coordinate_merge_sort(points, 'y')

#print(p_x)
ClosestPair(p_x, p_y)

'''

def test(px, py):
    lenpx = len(px)
    halflen = lenpx//2

    lx = px[:halflen]
    ly = coordinate_merge_sort(px[:halflen],'y')
    rx = px[halflen:]
    ry = coordinate_merge_sort(px[halflen:],'y')
    print(lx, ly, rx, ry)

test(p_x,p_y)

'''

#print(ClosestSplitpPair(p_x, p_y, 1))