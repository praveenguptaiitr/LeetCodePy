class Solution(object):

    def word_layout(self, word):
        d = dict()
        l = []
        cnt = 0
        for i,e in enumerate(word):
            if e in d:
                l[d[e]].append(i)
            else:
                d[e]=cnt
                cnt = cnt + 1
                k = []
                l.append(k)
                l[len(l)-1].append(i)

        return l


    def findAndReplacePattern(self, words, pattern):
        ans = []
        l = self.word_layout(pattern)
        for w in words:
            m = self.word_layout(w)
            if l==m:
                ans.append(w)

        return ans



if __name__ == '__main__':
    s = Solution()
    words = ["badc","abab","dddd","dede","yyxx"]
    pattern = "baba"
    print(s.findAndReplacePattern(words,pattern))