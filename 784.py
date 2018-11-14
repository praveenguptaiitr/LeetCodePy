class Solution(object):
    def __init__(self):
        self.ans = []

    def permute(self, s, i):
        if i > len(s):
            return
        if i == len(s):
            self.ans.append(s)
        for i in range(i,len(s)):
            self.permute(s, i + 1)
            if s[i].isalpha():
                if s[i].islower():
                    s1 = s[:i]+ s[i].upper()+s[i+1:]
                else:
                    s1 = s[:i]+ s[i].lower()+s[i+1:]
                self.permute(s1,i+1)



    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) is 0:
            return [""]
        self.ans.append(S)
        self.permute(S,0)
        return list(set(self.ans))

if __name__ == "__main__":
    s = Solution()
    print(s.letterCasePermutation("C"))
    #print(s.ans)