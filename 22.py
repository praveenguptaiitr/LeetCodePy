class Solution:
    def __init__(self):
        self.ans = []

    def bt(self, arr, k, lc, rc):
        if k==len(arr):
            if lc == rc:
                p = arr[:]
                p1 = "".join(arr)
                self.ans.append(p1)
        else:
            c = ["(", ")"]

            for i in range(len(c)):
                if c[i]=="(":
                    arr[k]=c[i]
                    self.bt(arr, k+1, lc+1, rc)
                elif c[i]==")" and rc < lc:
                    arr[k]=c[i]
                    self.bt(arr, k+1, lc, rc+1)



    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        arr = [""]*(2*n)
        self.bt(arr, 0, 0, 0)

        return self.ans

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))