class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

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
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1, 4],[4,5]]))
    print(s.merge([[1, 4], [1, 4]]))
    print(s.merge([[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]]))