class Solution(object):
    def partitionLabels(self, S):
        """
            :type S: str
            :rtype: List[int]
            """

        d = {}
        for k,v in enumerate(S):
            d[v]= max(d.get(v,-1), k)

        print(str(d))
        anchor = 0
        j = 0
        ans = []
        for i in range(len(S)):
            j = max(j,d[S[i]])
            if i == j:
                ans.append(j-anchor+1)
                anchor=j+1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
