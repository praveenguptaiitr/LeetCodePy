class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        t = K
        start = 0
        end = 0
        n = len(A)

        sz = float("-inf")
        if t < 0:
            return 0

        if t ==0 :
            while(end < n):
                while start< n and A[start]==0:
                    start+=1;
                end=start
                while(end < n and A[end]!=0):
                    end+=1
                sz = max(sz, end - start)
                start=end


        else:
            while(True):
                while(t>0 and end < n):
                    if A[end]==0:
                        t-=1
                    end+=1
                    if t==0:
                        while end < n and A[end]!=0:
                            end+=1

                if t ==0:
                    sz = max(end-start, sz)

                if end >= n:
                    break

                while(t==0 and start < end):
                    if A[start]==0:
                        t+=1
                    start+=1
        if sz == float("-inf") and t != 0:
            sz = n
        return sz



if __name__ == "__main__":
    s = Solution()

    #print(s.longestOnes([0,0,1,1,1,0,0],0))
    print(s.longestOnes([1,1,1,0,0,0,1,1,1,1],0))
    #print(s.longestOnes([0,0,0,1], 4))
    #print(s.longestOnes([0,0,1,1,1,0,0],0))

    #print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
    #print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

