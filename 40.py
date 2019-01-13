class Solution(object):
    def __init__(self):
        self.ans = {}

    def bt(self,candidates, target, arr, k, sum):
        if k == len(candidates) and sum != target:
            return

        if sum > target:
            return

        if sum==target:
            p = arr[:]
            p.sort()
            p1 = [str(i) for i in p]
            k1 = "".join(p1)
            self.ans[k1]=p

        else:
            c = [0,1]
            for i in range(len(c)):
                if c[i]==0:
                    self.bt(candidates, target, arr, k+1, sum)
                elif c[i]==1:
                    arr.append(candidates[k])
                    self.bt(candidates, target, arr, k+1, sum+candidates[k])
                    arr.pop()


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)==0:
            return []

        if len(candidates)==1 :
            if target==candidates[0]:
                return [candidates[0]]
            else:
                return []
        self.ans={}
        arr = []
        sum = 0
        self.bt(candidates, target, arr, 0, sum)
        return  self.ans.values()


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([2,5,2,1,2], 5))
    print(s.combinationSum2([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12],
    27))