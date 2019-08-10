class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        x = 0
        while x < len(intervals)-1:
            i,j = intervals[x+1][0],intervals[x+1][1]
            start,end = intervals[x][0],intervals[x][1]
            if start<=j and end>=i:
                intervals[x][0]= min(i,start)
                intervals[x][1]= max(j,end)
                del intervals[x+1]
            else:
                x+=1

        return intervals


if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1,3],[6,9]], [2,5]))
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))