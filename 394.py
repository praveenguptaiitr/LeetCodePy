class Solution(object):
    def __init__(self):
        self.ans = ""

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.helper(s)
        #return self.ans


    def helper(self,s):

        if s == "" or len(s)==1 or "[" not in s:
            return s

        start = 0
        first = True
        n = len(s)
        i=0
        d = 0
        j = 0
        ans = ""
        while i < len(s):
            j = i
            if i < n and '0' <= s[i] <= '9':
                j = i+1
                while j < n and '0' <= s[j] <= '9':
                    j+=1

                d = int(s[i:j])

            if i < n and 'a'<= s[i] <= 'z':
                ans+=s[i]
                i+=1
                continue

            i = j
            if s[j] == "[":
                count = 1
                j+=1
                while j < n and count > 0:
                    if s[j]=="]":
                        count-=1
                    if s[j]=="[":
                        count+=1
                    j+=1

            ans += d*(self.helper(s[i+1:j-1]))
            i=j


        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a2[c]]"))
    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("2[abc]3[cd]ef"))