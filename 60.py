import math
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = []
        for i in  range(1, n+1):
            numbers.append(i)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            del numbers[index]


        return permutation
if __name__ == "__main__":
    s = Solution()
    print(s.getPermutation(3,2))