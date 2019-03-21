class Solution(object):
    def __init__(self):
        self.path = []

    def dfs(self, u, graph, visited, path):
        if u == len(graph)-1:
            p = path[:]
            p.append(u)
            self.path.append(p)
        else:
            visited[u]=1
            path.append(u)
            for v in graph[u]:
                self.dfs(v,graph, visited,path )
            visited[u]=0
            path.pop()

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        visited = [0]*n
        path = []
        self.dfs(0, graph, visited, path)
        return self.path

if __name__ =="__main__":
    s = Solution()
    print(s.allPathsSourceTarget([[1,2], [3], [3], []] ))