class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        ans = ""
        while num > 0:
            if num >= 1000:
                n1 = num // 1000
                ans += n1*"M" if n1 > 1 else "M"
                num %=1000

            if num >= 900:
                n1 = num // 900
                ans += n1*"CM" if n1 > 1 else "CM"
                num %=900

            if num >= 500 :
                n1 = num//500
                ans +=n1*"D" if n1 > 1 else "D"
                num %=500

            if num >= 400 :
                n1 = num//400
                ans += n1*"CD" if n1 > 1 else "CD"
                num %=400

            if num >= 100:
                n1 = num//100
                ans +=n1*"C" if n1 > 1 else "C"
                num %=100

            if num >= 90:
                n1 = num//90
                ans +=n1*"XC" if n1 > 1 else "XC"
                num %=90

            if num >= 50:
                n1 = num//50
                ans +=n1*"L" if n1 > 1 else "L"
                num %=50
            if num >= 40:
                n1 = num//40
                ans +=n1*"XL" if n1 > 1 else "XL"
                num %=40

            if num >= 10:
                n1 = num//10
                ans +=n1*"X" if n1 > 1 else "X"
                num -=n1*10
            if num >= 9:
                n1 = num//9
                ans +=n1*"IX" if n1 > 1 else "IX"
                num %=9

            if num >= 5:
                n1 = num//5
                ans +=self.intToRoman(n1) + "V" if n1 > 1 else "V"
                num -=n1*5
            if num >= 4:
                n1 = num//4
                ans +=n1*"IV" if n1 > 1 else "IV"
                num %=4

            if num >= 1:
                n1 = num//1
                ans +=n1*"I" if n1 > 1 else "I"
                num =0

            return ans


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(4))
    print(s.intToRoman(9))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))