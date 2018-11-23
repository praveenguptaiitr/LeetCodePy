class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d = {}
        for c in p:
            d[c]=d.get(c,0)+1

        ctr = len(d)
        begin = 0
        end = 0
        l = 99999
        ans = []
        while( end < len(s)):
            if s[end] in d:
                d[s[end]]-=1
                if d[s[end]] == 0:
                    ctr -=1

            end+=1
            while(ctr == 0):
                if (end-begin == len(p)):
                    ans.append(begin)

                if s[begin] in d:
                    d[s[begin]]+=1
                    if d[s[begin]] > 0:
                        ctr+=1

                begin+=1

        return ans


