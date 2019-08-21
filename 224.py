class Solution(object):


    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        sign = 1
        number = 0
        stack = []

        for c in  s :
            if c.isdigit():
                number = number * 10 + (int(c) - int('0'))
            elif c == '+' :
                result += sign * number
                sign = 1
                number = 0
            elif c == '-':
                result += sign * number
                sign = -1
                number = 0
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result += sign * number
                number = result
                sign = stack.pop()
                result = stack.pop()

        result += sign * number
        return result



if __name__ == "__main__":
    s = Solution()
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
    print(s.calculate("2 - 1 + 2"))
    print(s.calculate("(7)-(0)+(4)"))
    #print(s.calculate("(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))"))