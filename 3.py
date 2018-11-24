class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        d = {}
        begin = 0
        end = 0
        l = 1
        while  end < len(s):

            if s[end] in d and d[s[end]]>= begin:
                # do something
                begin = d[s[end]]+1
                del d[s[end]]
            else:
                d[s[end]]=end
                end+=1

            l = max(l,end-begin)
        return l


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("tmmzuxt"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(" "))
    print(s.lengthOfLongestSubstring("au"))
    print(s.lengthOfLongestSubstring("abba"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("abcabcbb"))

