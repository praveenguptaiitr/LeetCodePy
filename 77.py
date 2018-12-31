class Solution:
    def __init__(self):
        self.ans = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        if n ==0:
            return 0
        if n==1:
            return [[1]]

        data = []
        m = 2 ** n
        for i in range(1,n+1):
            data.append(i)

        for i in range(0,m):
            s = bin(i)
            c = s[2:]
            c = c[::-1]
            p = []
            if s.count("1")==k:
                for j in range(len(c)):
                    if c[j]=="1":
                        p.append(data[j])

                self.ans.append(p)

        return self.ans

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4,1))