class Solution(object):
    def bt(self,nums, target, k, used, s, idx):
        if idx == len(nums):
            return False
        if k == 1:
            return True
        if k < 1:
            return False
        if s==target:
            return self.bt(nums,target, k-1, used, 0, idx)
        else:
            for i in range(idx,len(nums)):
                if used[i]==1:
                    continue
                if nums[i]>target:
                    return False
                if s+nums[i]<= target:
                    used[i] = 1
                    if self.bt(nums, target, k, used, s+nums[i], idx)== True:
                        return True
                    else:
                        used[i]=0
        return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = 0
        for i in nums:
            s+=i

        if s%k != 0 :
            return False
        if len(nums)==0:
            return False

        target = s/k
        nums.sort(reverse=True)
        if len(nums)==1 and k==1:
            if target==nums[0]:
                return True
            else:
                return False
        s = 0
        used = [0]*len(nums)
        return self.bt(nums, target, k, used, 0, 0)

if __name__ =="__main__":
    s = Solution()
    print(s.canPartitionKSubsets([85,35,40,64,86,45,63,16,5364,110,5653,97,95],7))
    # print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    # print(s.canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6],3))
    # print(s.canPartitionKSubsets([9,10,1,7,2,7,1,1,1,3],3))
    # print(s.canPartitionKSubsets([3522, 181, 521, 515, 304, 123, 2512, 312, 922, 407, 146, 1932, 4037, 2646, 3871, 269],5))