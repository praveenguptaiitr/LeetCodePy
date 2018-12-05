class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        ans = {}
        d = {}

        if k==0:
            for i in nums:
                d[i]=d.get(i,0)+1

            sum = 0
            for k,v in d.items():
                if v>1:
                    sum+=1

            return int(sum)
        else:
            for i in nums:
                d[i]=1

            for i in nums:

                if d.get(i-k,-99999)!=-99999:
                    ans[i]=1

        return len(ans)

if __name__ == "__main__":
    s = Solution()
    print(s.findPairs([1, 3, 1, 5, 4], 0))