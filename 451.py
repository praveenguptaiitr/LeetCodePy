import operator
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        d = {}
        for i in s:
            d[i] = d.get(i,0)+1

        ans = []
        x = sorted([(v,k) for k,v in d.items()],reverse=True)
        for k,v in x:
            s = v*k
            ans.append(s)

        return "".join(ans)

if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("Aabb"))