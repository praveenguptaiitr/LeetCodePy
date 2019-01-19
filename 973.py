from functools import cmp_to_key

def cmp(a,b):
    a1 = (a[0]**2) + (a[1]**2)
    b1 = (b[0]**2) + (b[1]**2)
    if a1 < b1:
        return -1
    elif a1==b1:
        return 0
    else:
        return 1

class Solution(object):

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        c = cmp_to_key(cmp)
        points.sort(key=c)
        return points[:K]
