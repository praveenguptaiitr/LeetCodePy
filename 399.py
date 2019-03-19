class Solution(object):
    def __init__(self):
        self.ans = []
        self.found = False

    def dfs(self, n, d, adj, visited, scr):
        if n == d and self.found!=True:
            self.ans.append(scr)
            self.found=True
        else:
            visited[n]=1
            for e in adj[n]:
                if visited[e[0]]!=1:
                    self.dfs(e[0], d, adj, visited, scr*e[1])
            visited[e[0]]=0

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj = {}
        for i in range(len(equations)):
            e = equations[i]
            if adj.get(e[0],None)==None:
                adj[e[0]]=[]

            if adj.get(e[1],None)==None:
                adj[e[1]]=[]

            adj[e[0]].append((e[1],values[i]))
            adj[e[1]].append((e[0],1/values[i]))

        print(adj)
        ans = []
        for q in queries:
            n = q[0]
            d = q[1]
            if n not in adj or d not in adj:
                self.ans.append(-1)
                continue
            if n == d:
                self.ans.append(1)
                continue

            visited = {}
            for k in adj:
                visited[k]=0
            scr  = 1
            self.dfs(n,d,adj, visited, scr)
            if self.found==False:
                self.ans.append(-1)
            else:
                self.found=False
        #print(len(self.ans))
        #print(len(queries))
        return self.ans

if __name__ == "__main__":
    s = Solution()
    #print(s.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
    #print(s.calcEquation([["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],[3.0,0.5,3.4,5.6],[["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]))
    #print(s.calcEquation([["a","b"], ["c","d"]],[1,1], ))

    print(s.calcEquation([["a","b"],["a","c"],["a","d"],["a","e"],["a","f"],["a","g"],["a","h"],["a","i"],["a","j"],["a","k"],["a","l"],["a","aa"],["a","aaa"],["a","aaaa"],["a","aaaaa"],["a","bb"],["a","bbb"],["a","ff"]],
[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,1.0,1.0,1.0,1.0,1.0,3.0,5.0],
[["d","f"],["e","g"],["e","k"],["h","a"],["aaa","k"],["aaa","i"],["aa","e"],["aaa","aa"],["aaa","ff"],["bbb","bb"],["bb","h"],["bb","i"],["bb","k"],["aaa","k"],["k","l"],["x","k"],["l","ll"]]))
