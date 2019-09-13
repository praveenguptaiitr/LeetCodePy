from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        n = len(s)
        if n == 0:
            return 0
        if n < k:
            return n
        if k == 0:
            return 0
        if len(set(s)) <= k:
            return n

        start = 0
        end = 0
        d = defaultdict(int)
        mlen = float("-inf")
        counter = 0
        while end < n:
            c = s[end]
            d[c]+=1
            if d[c]==1:
                counter+=1

            end+=1
            while counter > k:
                c = s[start]
                if c in d:
                    d[c]-=1
                    if d[c]==0:
                        counter-=1

                start+=1
            mlen = max(mlen, end-start)
        return mlen



if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstringKDistinct("eceba", 2))
    print(s.lengthOfLongestSubstringKDistinct("bacc",2))
    print(s.lengthOfLongestSubstringKDistinct("aa", 1))