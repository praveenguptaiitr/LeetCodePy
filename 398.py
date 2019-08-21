class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.arr = [(nums[i],i) for i in range(len(nums))]
        self.arr.sort(key=lambda x : x[0])
        print(self.arr)
        self.ans = [-1]*2

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        self.bs(0, self.n-1, target)
        l = []
        for i in self.arr[self.ans[0]:self.ans[1]+1]:
            l.append(i[1])

        import random
        p = random.randint(len(l)-1)
        return l[p]
        #print(self.ans)

    def bs(self, l, r, target):
        if l > r:
            return -1

        if l == r:
            if self.arr[l][0]==target:
                if self.ans==-1 or l < self.ans[0]:
                    self.ans[0]=l
                if self.ans==-1 or r > self.ans[1]:
                    self.ans[1]=r
                return l
            else:
                return -1


        mid = (l+r)//2

        if self.arr[mid][0]==target:
            if self.ans[0] == -1 or mid < self.ans[0]:
                self.ans[0] = mid
            if self.ans[1] == -1 or mid > self.ans[1]:
                self.ans[1] = mid

            k = self.bs(l, mid-1, target)
            if k!= -1 and k < self.ans[0]:
                self.ans[0]=k

            k = self.bs(mid + 1, r, target)
            if k != -1 and k > self.ans[1]:
                self.ans[1] = k
            return mid

        elif self.arr[mid][0] > target:
            return self.bs(l, mid - 1, target)
        else:
            return self.bs(mid + 1, r, target)


if __name__ == "__main__":
    s = Solution([3,2,3,1,3])
    print(s.pick(3))