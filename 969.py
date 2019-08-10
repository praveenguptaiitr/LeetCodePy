class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        if len(A)==1:
            return []

        n = len(A)
        k = n
        ans = []
        while k > 0:
            m = max(A[:k])
            if m != A[k-1]:
                m1 = A.index(m)
                B = A[:m1+1] #+ A[m1:]
                B.reverse()
                A = B + A[m1+1:]
                ans.append(m1+1)
                ans.append(k)
                B = A[:k]
                B.reverse()
                #A = B + A[k+1:]
                A = B
                k-=1
            else:
                k -=1

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.pancakeSort([3,2,4,1]))
    print(s.pancakeSort([1,2,3]))

