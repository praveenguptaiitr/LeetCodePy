class Solution(object):
    def __init__(self):
        self.set = {}
    def make_set(self, v):
        if v not in self.set:
            self.set[v]=v
    def find(self, v):
        if self.set[v]==v:
            return v
        return self.find(self.set[v])

    def union(self, u, v):
        a = self.find(u)
        b = self.find(v)
        if a != b:
            self.set[b]=a

    def connected(self, a, b):
        if self.find(a)==self.find(b):
            return True
        else:
            return False

    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        eq = []
        n_eq = []
        for e in equations:
            if "!" in e:
                n_eq.append(e)
            else:
                eq.append(e)

        for e in eq:
            a = e[0]
            b = e[3]
            if a not in self.set:
                self.make_set(a)
            if b not in self.set:
                self.make_set(b)

            self.union(a,b)
        for e in n_eq:
            a = e[0]
            b = e[3]
            if a not in self.set:
                self.make_set(a)
            if b not in self.set:
                self.make_set(b)

            if self.connected(a,b):
                return False

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.equationsPossible(["a==b","b!=a"]))
    print(s.equationsPossible(["b==a","a==b"]))
    print(s.equationsPossible(["a==b","b==c","a==c"]))
    print(s.equationsPossible(["a==b","b!=c","c==a"]))
    print(s.equationsPossible(["c==c","b==d","x!=z"]))


if __name__=="__main__":
    s = Solution()
    s.equationsPossible(["a==b","b!=a"])