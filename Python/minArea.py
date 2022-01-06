#!/bin/python3
import os

# Complete the 'minArea' function below.
# The function is expected to return an INTEGER.
# Since the argument is from std in, a string is passed
# The function conceptually accepts LIST of n pairs of [x, y] data as parameter.
# e.g. [[1, 2], [2, 3], [3, 4]]
# The first step of converting str(list) -> list is provided
import collections
import json

def smallerLst(lst, val, i):
    lo, hi = 0, len(lst)-1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if lst[mid][i] < val:
            lo = mid
        else:
            hi = mid - 1
    return hi

def minArea(data_lst):
    # data = eval(data_str)

    # data_lst = json.loads(data_str)
    # print(data_lst)
        
    data_lst.sort()
    xcoords = {}
    ycoords = {}
    ans = float('inf')
    for p in data_lst:
        x, y = p
        needCheck = True
        if x not in xcoords:
            xcoords[x] = [p]
            needCheck = False
        else:
            xcoords[x].append(p)
        
        if y not in ycoords:
            ycoords[y] = [p]
            needCheck = False
        else:
            ycoords[y].append(p)

        # if not needCheck:
        #     continue
        
        down = xcoords[x][:smallerLst(xcoords[x], y, 1)+1]
        left = ycoords[y][:smallerLst(ycoords[y], x, 0)+1]

        for pd in reversed(down):
            yp = pd[1]
            for pl in reversed(left):
                xp = pl[0]
                print(xp, ":", yp)
                if [xp,yp] in data_lst:
                    ans = min(ans, (yp-y)*(xp-x))
                    print(ans)
                    break
            else:
                continue
            break
                    
    ans = 0 if ans == float('inf') else ans
    return ans

def minAreaRect(points) -> int:
    x_dict = collections.defaultdict(set)
    y_dict = collections.defaultdict(set)
    for point in points:
        x, y = point
        x_dict[x].add(y)
        y_dict[y].add(x)
    x_list = []
    print(x_dict)
    for key in x_dict:
        if len(x_dict[key]) >= 2:
            x_list.append(key)      
    x_list.sort()
    ans = float('inf')
    for i in range(len(x_list)-1):
        # pick two points
        set_left = x_dict[x_list[i]]
        for j in range(i+1, len(x_list)):
            # find common set
            set_right = x_dict[x_list[j]]
            intersect = list(set_left & set_right)
            if len(intersect) >= 2:
                intersect.sort()
                for k in range(1, len(intersect)):
                    ans = min(ans, (x_list[j] - x_list[i]) * abs(intersect[k] - intersect[k-1]))
    return ans if ans != float('inf') else 0

def minAreaRect2(points) -> int:
    
    point_set=set([(p[0],p[1]) for p in points])
    output=float('inf')
    
    for bl in point_set:
        blx,bly=bl[0],bl[1]
        for tr in point_set:
            if bl[0]<tr[0] and bl[1]<tr[1]:
                tl=(bl[0],tr[1])
                br=(tr[0],bl[1])
                if tl in point_set and br in point_set:
                    area=(br[0]-bl[0])*(tl[1]-bl[1])
                    output=min(area,output)
    
    return output if output<float('inf') else 0

if __name__ == '__main__':

    data = "[[-1, -1], [0, 0]]"
    data = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]

    result = minArea(data)

    print(result)