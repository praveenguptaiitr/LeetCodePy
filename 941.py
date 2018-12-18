class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)==0 or len(A)==1 or len(A)==2:
            return False

        isMountain = False
        for i in range(1,len(A)-1):
            if A[i-1]==A[i]:
                return False
            if A[i-1]< A[i] and A[i]>A[i+1] :
                if isMountain==False:
                    isMountain=True
                else:
                    return False
            if A[i-1]> A[i] and A[i+1]>A[i]:
                return False

        return isMountain


if __name__=="__main__":
    s = Solution()
    print(s.validMountainArray([0,1,2,1,2]))