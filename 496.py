class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(findNums)==0:
            return []
        if len(nums)==0:
            return []

        ans = []
        found = False
        for j in range(len(findNums)):
            found = False
            k = nums.index(findNums[j])
            for i in range(k+1,len(nums)):
                if nums[i]>findNums[j]:
                    ans.append(nums[i])
                    found = True
                    break

            if found == False:
                ans.append(-1)

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElement([4,1,2],[1,3,4,2]))