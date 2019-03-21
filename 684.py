class Solution(object):
    def __init__(self):
        self.redSet = []
        self.set = {}

    def make_set(self, u):
        if u not in self.set:
            self.set[u]=u

    def find(self, u):
        if self.set[u]==u:
            return u
        else:
            return self.find(self.set[u])

    def union(self, u , v):
        a = self.find(u)
        b = self.find(v)
        if a!=b:
            self.set[a]=b

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        for e in edges:
            u = e[0]
            v = e[1]
            self.make_set(u)
            self.make_set(v)
            a = self.find(u)
            b = self.find(v)
            if a == b:
                self.redSet.append(e)
            self.union(u,v)

        return sorted(self.redSet[-1])

if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantConnection([[1,2], [1,3], [2,3]]))
    print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))