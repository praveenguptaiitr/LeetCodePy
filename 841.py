class Solution(object):

    def dfs(self, u, rooms, visited):
        if visited[u]==1:
            return
        visited[u]=1
        for v in rooms[u]:
            if visited[v]!=1:
                self.dfs(v,rooms,visited)

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        n = len(rooms)
        visited = [0]*n
        self.dfs(0, rooms, visited)
        for i in range(n):
            if visited[i] == 0:
                return False

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.canVisitAllRooms([[1],[2],[3],[]]))
    print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))