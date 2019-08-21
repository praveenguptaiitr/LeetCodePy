class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = 0
        sign = '+'
        number = 0
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                number = number*10 + int(s[i])-int('0')
            if i+1 == len(s) or (s[i]=='+' or s[i]=='-' or s[i]=='*' or s[i] == '/'):
                if sign=="+":
                    stack.append(number)
                elif sign=="-":
                    stack.append(-number)
                elif sign=="*":
                    stack[-1] = stack[-1] * number
                elif sign=="/":
                    stack[-1] = int(stack[-1] / float(number))

                sign = s[i]
                number = 0

        return sum(stack)



if __name__ == "__main__":
    s = Solution()
    print(s.calculate("14-3/2"))
