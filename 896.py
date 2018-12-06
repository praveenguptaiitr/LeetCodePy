class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        if len(A)==0 or len(A)==1 or len(A)==2:
            return True


        idx  = 0
        while(idx < len(A)-2 and A[idx]==A[idx+1]):
            idx+=1

        if idx == len(A)-2:
            return True

        d = (A[idx]-A[idx+1])>0
        for i in range(idx, len(A)-1):
            if (A[i]==A[i+1]):
                continue
            if ( (A[i]-A[i+1]>=0) != d):
                return False

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isMonotonic([1,1,1]))
