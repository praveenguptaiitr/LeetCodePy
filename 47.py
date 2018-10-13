
class Solution(object):

    def perm(self, nums, i,st):
        if i == len(nums)-1:
            l2 = list(nums)
            st["".join(str(nums))]=l2
            #l1.append(l2)
            return

        for k in range(i,len(nums)):
            nums[i], nums[k] = nums[k], nums[i]
            self.perm(nums,i+1,st)
            nums[i], nums[k] = nums[k], nums[i]

        return

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l1 = list()
        st = dict()
        self.perm(nums,0,st)
        #print(str(st))
        for k,v in st.items():
            l1.append(v)
        return (l1)


if __name__=="__main__":
    s = Solution()
    l = [1,1,2]

    print(s.permute(l))
