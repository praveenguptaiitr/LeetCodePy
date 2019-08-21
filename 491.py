class Solution:
    def __init__(self):
        self.ans = {}


    def construct_candidates(self, k, nums, curr):
        c = []
        for j in range(k, len(nums)):
            if nums[j]>= nums[k] and nums[j]>= curr[-1]:
                c.append(j)

        return c

    def helper(self, k , curr, nums):

            if k > len(nums):
                p = curr[:]
                if len(p)>1:
                    s = "".join([str(i) for i in p])
                    self.ans[s]=p
                return


            else:
                if len(curr)>1:
                    a = curr[:]
                    s = "".join([str(i) for i in a])
                    self.ans[s]=a
                c = self.construct_candidates(k+1, nums, curr)
                for i in c:
                    curr.append(nums[i])
                    self.helper(i,curr, nums )
                    curr.pop()



    def findSubsequences(self, nums):
        if len(nums)==0 or len(nums)==1:
            return [nums]

        curr = []
        for i in range(len(nums)):
            curr=[]
            curr.append(nums[i])
            self.helper(i, curr, nums)
            curr.pop()
        return self.ans.values()




if __name__ == "__main__":
    s = Solution()
    #print(s.findSubsequences([4,3,2,1]))
    #print(s.findSubsequences([4, 6,7,7]))
    print(s.findSubsequences([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))