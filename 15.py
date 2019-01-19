class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if len(nums)==0:
            return []

        if len(nums)<3:
            return []

        if len(nums)==3:
            if sum(nums)==0:
                return [nums]
            else:
                return []

        ans = {}
        nums.sort()
        for i in range(n):
            start = i+1
            end = n-1
            target = -nums[i]
            curr = []
            while(start<n and end>=0 and start<end):
                if (nums[start]+ nums[end]==target):
                    curr=[-target, nums[start], nums[end]]
                    curr.sort()
                    c2 = curr[:]
                    c1 = [str(i) for i in curr]
                    s1 = "".join(c1)
                    ans[s1]= curr
                    start+=1
                    continue
                elif (nums[start]+ nums[end]<target):
                    start+=1
                else:
                    end-=1

        return ans.values()

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-2,0,1,1,2]))