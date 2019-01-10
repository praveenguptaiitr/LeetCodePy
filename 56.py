from functools import cmp_to_key

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def cmp_items(a,b):
    if a.start < b.start:
        return -1
    elif a.start == b.start:
        if a.end < b.end:
            return -1
        elif a.end == b.end:
            return 0
        else:
            return 1
    else:
        return 1

class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0 or len(intervals)==1:
            return intervals

        cmp_items_py3 = cmp_to_key(cmp_items)

        intervals.sort(key=cmp_items_py3)
        for i in intervals:
            print(str(i.start) + " - " + str(i.end))
        print("----------")
        mrg = True
        while mrg==True:
            mrg = False
            i = 0
            while i < len(intervals)-1:
                #print(str(intervals[i].start) + " - " + str(intervals[i].end))
                if intervals[i].end>=intervals[i+1].start and intervals[i].end < intervals[i+1].end:
                    intervals[i].end = intervals[i+1].end
                    del intervals[i+1]
                    mrg = True
                else:
                    if intervals[i].end >= intervals[i + 1].start and intervals[i].end >= intervals[i + 1].end:
                        del intervals[i+1]
                        mrg = True
                i+=1
        return intervals

if __name__ == "__main__":
    s = Solution()
    l = []
    #[[5, 5], [1, 3], [3, 5], [4, 6], [1, 1], [3, 3], [5, 6], [3, 3], [2, 4], [0, 0]]
    l.append(Interval(5,5))
    l.append(Interval(1,3))
    l.append(Interval(3,5))
    l.append(Interval(4,6))

    l.append(Interval(1,1))
    l.append(Interval(3,3))
    l.append(Interval(5,6))
    l.append(Interval(3,3))
    l.append(Interval(2, 4))
    l.append(Interval(0, 0))

    ans = s.merge(l)
    print("================")
    for i in ans:
        print(str(i.start) + " - " + str(i.end))
