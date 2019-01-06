class Solution:
    def __init__(self):
        self.arr = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"],\
                    "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"],\
                    "8":["t","u","v"], "9":["w","x","y","z"]}
        self.ans = []

    def construct_candidates(self, i):
        return self.arr[i]

    def bt(self, digits, k, arr):

        if k==len(digits):
            p = arr[:]
            p1 = "".join(arr)
            self.ans.append(p1)
        else:
            c =self.construct_candidates(digits[k])
            for i in range(len(c)):
                arr[k]=c[i]
                self.bt(digits,k+1,arr)

        return

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        if len(digits)==1:
            return self.arr[digits[0]]

        arr = [""]*len(digits)
        self.bt(digits, 0, arr)

        return self.ans

if __name__ =="__main__":
    s = Solution()
    print(s.letterCombinations("23"))
