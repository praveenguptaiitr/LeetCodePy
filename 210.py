class Solution(object):
    def dfs(self, vert, adj, visited, order):
        if visited[vert]==1:
            return False
        if visited[vert]==2:
            return True
        visited[vert] = 1
        no_cycle = True
        if len(adj[vert])!=0:
            for i in adj[vert]:
                if visited[i]==1:
                    return False
                ans = self.dfs(i, adj, visited, order)
                if ans==False:
                    no_cycle=False
        if no_cycle==False:
            return False
        visited[vert]=2
        order.insert(0,vert)
        return True


    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for i in range(numCourses)]
        for i in prerequisites:
            adj[i[1]].append(i[0])

        v = [ i for i in range(numCourses)]
        visited = [0]*numCourses
        order = []
        no_cycle =True
        for i in range(numCourses):
            if visited[i]==0:
                ans = self.dfs(i, adj, visited, order)
                if ans == False:
                    no_cycle=False
        if no_cycle==False:
            return []
        else:
            return order

if __name__ == "__main__":
    s = Solution()
    #print(s.findOrder(2, [[1,0]] ))
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    #print(s.findOrder(2, [[0,1],[1, 0]]))