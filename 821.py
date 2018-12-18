class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        j = []
        for i in range(len(S)):
            if S[i]==C:
                j.append(i)
        ans = []
        for i in range(len(S)):
            ans.append(min([abs(i-k) for k in j]))

        return ans
