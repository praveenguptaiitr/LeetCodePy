class Solution(object):
    def __init__(self):
        self.ans = [-1]*2

    def search(self, nums, l, h, target):
        if l>h:
            return -1

        if l==h :
            if nums[l]== target:
                if self.ans[0]==-1 or l < self.ans[0]:
                    self.ans[0]=l
                if self.ans[1] == -1 or l> self.ans[1]:
                    self.ans[1] = l
                return l
            else:
                return -1


        mid = (l+h)//2
        if nums[mid]==target:
            if self.ans[0]==-1 or  mid < self.ans[0]:
                self.ans[0] = mid
            if self.ans[1]==-1 or mid > self.ans[1]:
                self.ans[1] = mid

            k=self.search(nums, l, mid-1, target)
            if k != -1 and k < self.ans[0]:
                self.ans[0]=k

            k =self.search(nums, mid+1, h, target)
            if k!=-1 and k > self.ans[1]:
                self.ans[1]=k
            return mid

        elif nums[mid]>target:
            return self.search(nums, l, mid-1, target)
        else:
            return self.search(nums, mid+1, h , target)

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ans = [-1,-1]
        if len(nums)==0:
            return ans
        if len(nums)==1 and nums[0]==target:
            return [0,0]

        self.search(nums, 0, len(nums)-1,target)
        self.ans.sort()
        return self.ans

if __name__=="__main__":
    s = Solution()
    print(s.searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10],4))
