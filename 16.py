class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if len(nums)==0:
            return 0

        if len(nums)<3:
            sum(nums)

        if len(nums)==3:
            return sum(nums)

        ans = {}
        nums.sort()
        diff = 999999
        for i in range(n):
            start = i+1
            end = n-1
            #t = target-nums[i]
            while(start<n and end>=0 and start<end):
                s = nums[i]+ nums[start]+ nums[end]
                if abs(target-diff)>abs(s-target):
                    diff = s
                if s < target:
                    start+=1
                else:
                    end-=1

        return diff

if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest( [-1, 2, 1, -4], 1))