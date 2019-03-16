class Solution(object):
    def dfs(self, u, d, n, tickets, ans):
        if u in d and len(d[u])>0:
            c = sorted(d[u])
            for i in c:
                ans.append(i)
                d[u].remove(i)
                r = self.dfs(i, d, n+1, tickets, ans)
                if len(r) == len(tickets)+1:
                    return ans[:]
                else:
                    ans.pop(-1)
                    d[u].append(i)
        return ans

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = {}
        for t in tickets:
            u,v = t
            if d.get(u,-1)==-1:
                d[u]= []

            d[u].append(v)

        s =  "JFK"
        n = 0
        ans = []
        ans.append(s)
        #ans = [""]*len(tickets)

        self.dfs(s,d,n, tickets, ans)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
    print(s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
