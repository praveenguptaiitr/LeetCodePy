from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)==0:
            return [[]]
        d = dict([])
        for s in strs:
            k = "".join(sorted(s))
            p = d.get(k,-1)
            if p ==-1:
                d[k]=[s]
            else:
                d[k].append(s)

        ans = []
        for _,v in d.items():
            ans.append(v)

        return ans

if __name__=="__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))