class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        j = 0
        sat = 0
        for i in range(len(g)):
            while (j < len(s) and s[j] < g[i]):
                j+=1
            if j>=len(s):
                break
            sat+=1
            j+=1

        return sat

if __name__ == "__main__":
    s = Solution()
    print(s.findContentChildren([1,2,3], [1,1]))
    print(s.findContentChildren([1,2], [1,2,3]))
