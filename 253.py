class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if len(intervals)==0:
            return 0

        if len(intervals)==1:
            return 1

        intervals.sort(key = lambda x : x[0])

        rooms = []
        rooms.append((intervals[0][0], intervals[0][1]))
        for x in range(1, len(intervals)):
            start, end = intervals[x][0], intervals[x][1]
            found = False
            for k in range(len(rooms)):
                if rooms[k][1]<= start:
                    del rooms[k]
                    rooms.append((start,end))
                    found = True
                    break

            if found == False:
                rooms.append((start, end))

        return len(rooms)


if __name__ == "__main__":
    s = Solution()
    print(s.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
    print(s.minMeetingRooms([[7,10],[2,4]]))
    print(s.minMeetingRooms([[13,15],[1,13]]))
    print(s.minMeetingRooms([[1080,2236],[3325,5014],[1397,3851],[54,1519],[1794,2238],[2907,4858]]))