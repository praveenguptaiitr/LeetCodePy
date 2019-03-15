class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left,right+1):
            c = str(i)
            sdn = i
            for j in c:
                k = int(j)
                if k==0 or i%k!=0:
                    sdn = -1
                    continue
            if sdn !=-1:
                ans.append(i)
        return ans