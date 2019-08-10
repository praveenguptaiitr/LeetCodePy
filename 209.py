class Solution:
    def minSubArrayLen(self, s, nums):
        if len(nums)==0:
            return 0

        if len(nums)==1 and nums[0]==s:
            return nums[0]

        if len(nums)==1 and nums[0]!=s:
            return 0

        start=0
        end=0
        sum=0
        ans1,ans2=float("-inf"),float("inf")
        while(end< len(nums) and start<=end):

            if sum+nums[end]  >= s:
                if ans2-ans1 > end-start:
                    ans1,ans2=start,end

                sum-=nums[start]
                start+=1
                continue
            else:
                sum+=nums[end]
            end+=1


        return nums[ans1:ans2+1]



if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(11, [1,2,3,4,5]))
