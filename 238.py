class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [0]* len(nums)
        output[len(nums)-1]= nums[len(nums)-1]
        for i in range(len(nums)-2,0,-1):
            output[i]=output[i+1]*nums[i]

        x = nums[0]
        output[0]=output[1]
        for i in range(1,len(nums)-1):
            output[i]=x*output[i+1]
            x = x*nums[i]
        output[len(nums)-1]=x
        return output

if __name__ == '__main__':
    s = Solution()
    s.productExceptSelf([9,0,-2])