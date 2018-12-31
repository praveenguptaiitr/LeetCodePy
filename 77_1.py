class Solution(object):
    def __init__(self):
        self.ans = []

    def bt(self,data,a, k, val ):
        c=[0,1]

        if k==len(data): # is a sol
            count = 0
            p = []
            for i in range(len(a)):
                if a[i]==1:
                    count+=1
                    if count > val:
                        break
                    else:
                        p.append(data[i])

            if count==val:
                self.ans.append(p)
        else:
            for i in range(2):
                a[k]=c[i]
                self.bt(data,a,k+1, val)

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
        for i in range(1,n+1):
            data.append(i)

        a = [0]*len(data)
        self.bt(data,a, 0, k)
        return self.ans

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4,2))