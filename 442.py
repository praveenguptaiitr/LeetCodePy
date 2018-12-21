class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                ans.append(abs(nums[i]))
            else:
                k = abs(nums[i])-1
                nums[k]*=-1

        return ans



if __name__=="__main__":
    s = Solution()
    print(str(s.findDuplicates([4,3,2,7,8,2,3,1])))