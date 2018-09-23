from coordinate_merge_sort import coordinate_merge_sort

def euclidean_dist(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def ClosestPair(px, py):
    lenpx = len(px)
    halflen = lenpx//2
    if len(px)>=3:
        lx = px[:halflen]
        ly = coordinate_merge_sort(px[:halflen],'y')
        rx = px[halflen:]
        ry = coordinate_merge_sort(px[halflen:],'y')

        best_l1, best_l2 = ClosestPair(lx, ly)             #best left pair
        best_r1, best_r2 = ClosestPair(rx, ry)             #best right pair
        left_min_dist = euclidean_dist(best_l1, best_l2)
        right_min_dist = euclidean_dist(best_r1, best_r2)

        delta = min(left_min_dist, right_min_dist)

        best_split, split_min_dist = ClosestSplitpPair(px, py, delta)      #best split pair

        distlist = [left_min_dist, right_min_dist, split_min_dist]
        coordlist = [[best_l1, best_l2], [best_r1, best_r2], best_split]
        bestindex = distlist.index(min(distlist))

        if best_split == None:
            return coordlist[distlist[:1].index(delta)]
        else:
            return coordlist[bestindex][0], coordlist[bestindex][1]
    else:
        return px[0], px[1]

def ClosestSplitpPair(px, py, delta):
    lenpx = len(px)
    halflen = lenpx//2
    xbar = px[halflen][0]

    sy = list()
    for i in py:
        if (xbar - delta) <= i[0] <= (xbar + delta):
            sy.append(i)

    best = delta
    bestPair = None

    i = 0
    j = 0

    while 1 < i < lenpx-1:
        while 1 < j < min(7, lenpx-i):
            temp_dist = euclidean_dist(sy[i], sy[i+j])
            if temp_dist < best:
                best = temp_dist
                bestPair = [sy[i], sy[i+j]]
            j+= 1
        i+= 1

    return bestPair, best
