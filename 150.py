class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens)==0:
            return None
        s = []
        for i in range(len(tokens)):
            if tokens[i]=="+":
                e1 = int(s.pop())
                e2 = int(s.pop())
                s.append(str(e1+e2))
                #pass
            elif tokens[i]=="-":
                e1 = int(s.pop())
                e2 = int(s.pop())
                s.append(str(e2-e1))
            elif tokens[i]=="*":
                e1 = int(s.pop())
                e2 = int(s.pop())
                s.append(str(e1*e2))
            elif tokens[i]=="/":
                e1 = int(s.pop())
                e2 = int(s.pop())
                s.append(str(int(e2/e1)))
            else:
                s.append(tokens[i])

        return int(s[0])

if __name__ == "__main__":
    s = Solution()
    #print(s.evalRPN(["2", "1", "+", "3", "*"]))
    #print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    #print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))