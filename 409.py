from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        # print(c)
        even = 0
        odd = 0
        for k, v in c.items():
            even += int(v / 2)
            odd += v % 2
        # print(even)
        # print(odd)
        if odd > 0:
            odd = 1
        return even * 2 + odd


if __name__ == "__main__":
    s = Solution()
    s.longestPalindrome("abccccdd")