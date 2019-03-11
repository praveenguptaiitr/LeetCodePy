class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        d=[0]*(N+1)
        tr= [0]*(N+1)
        for i in trust:
            u,v = i[0],i[1]
            d[u]+=1
            tr[v]+=1

        for i in range(1,N+1):
            if d[i]==0 and tr[i]==N-1:
                return i

        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.findJudge(2, [[1,2]]))
    print(s.findJudge(3, [[1,3],[2,3]]))
    print(s.findJudge(3, [[1,3],[2,3],[3,1]]))
    print(s.findJudge(3,[[1,2],[2,3]]))
    print(s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))