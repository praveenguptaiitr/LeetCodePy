class Solution(object):
    def bfs(self, graph, color, s):

        color[s]=0
        q = []
        q.append(s)
        while(len(q)>0):
            i = q.pop()
            for j in graph[i]:
                if color[j]==-1:
                    color[j]=1-color[i]
                    q.append(j)
                else:
                    if color[j]==color[i]:
                        return False

        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if len(graph)<=1:
            return True

        v = [-1]*len(graph)

        for i in range(len(graph)):
            if v[i]==-1:
                if self.bfs(graph, v, i) == False:
                    return False
        return True





if __name__ == "__main__":
    s = Solution()
    #print(s.isBipartite([[1,3], [0,2], [1,3], [0,2]]))
    #print(s.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
    print(s.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))