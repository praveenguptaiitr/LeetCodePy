class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if abs(num) == 2 ** 31:
            return False

        while num > 0:
            if num % 2 == 0:
                num //= 2
            elif num % 3 == 0:
                num //= 3
            elif num % 5 == 0:
                num //= 5
            else:
                break

        return num == 1

if __name__ == "__main__":
    s= Solution()
    print(s.isUgly(6))
    print(s.isUgly(8))
    print(s.isUgly(14))
