class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.replace("i","")
        b = b.replace("i","")

        l1 = a.split("+")
        l2 = b.split("+")

        ans1 =  int(l1[0])*int(l2[0]) - int(l1[1])*int(l2[1])
        ans2 = int(l1[0])*int(l2[1]) + int(l1[1])*int(l2[0])
        return ( str(ans1)+ "+" + str(ans2)+"i")
        #print(str(l1) + " -- " + str(l2))


if __name__ == "__main__":
    s = Solution()
    #s.complexNumberMultiply("1+1i", "1+1i")
    #s.complexNumberMultiply("1+-1i", "1+-1i")
    print(s.complexNumberMultiply("1+-1i","0+0i"))