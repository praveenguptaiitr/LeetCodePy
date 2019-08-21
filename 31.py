class Solution:
    def nextPermutation(self, nums):
        if 0<=len(nums)<=1:
            return

        s = True
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                s = False
                break

        if s == True:
            nums.sort()
            return

        i = len(nums)-2
        while (i >= 0) and nums[i]>= nums[i+1]:
            i-=1

        j = i+1
        m = nums[j]
        x = j
        while(j<len(nums)):
            if nums[j]>nums[i] and nums[j]<m:
                x=j
                m = nums[j]

            j+=1

        nums[i], nums[x]=nums[x], nums[i]


        m1 = nums[:i+1]
        m2 = sorted(nums[i+1:])
        x = m1+m2
        for i in range(len(x)):
            nums[i]= x[i]

        return



if __name__ == "__main__":
    s = Solution()
    #print(s.nextPermutation([1,5,8,4,7,6,5,3,1]))
    #print(s.nextPermutation([1,3,2]))
    print(s.nextPermutation([2,2,7,5,4,3,2,2,1]))