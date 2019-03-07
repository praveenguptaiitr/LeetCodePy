class Solution(object):
    def dfs(self, i, adj, visited):
        if visited[i] == 1:
            return True
        if visited[i] == 2:
            return False
        visited[i] = 1
        cycle = False
        for j in adj[i]:
            if visited[j] == 1:
                return True
            else:
                d = self.dfs(j, adj, visited)
                if d == True:
                    cycle = True
        visited[i] = 2
        return cycle

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        v = [i for i in range(numCourses)]
        adj = [[] for i in range(numCourses)]

        visited = [0] * numCourses
        for i in range(len(prerequisites)):
            e = prerequisites[i]
            adj[e[1]].append(e[0])
        # print(adj)
        cycle = False
        for i in range(numCourses):
            if visited[i] == 0:
                d = self.dfs(i, adj, visited)
                if d == True:
                    cycle = True
        return not cycle


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1,0]]))