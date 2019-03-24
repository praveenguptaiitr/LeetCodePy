class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        s = ("{:032b}".format(n))
        s = s[::-1]
        return int(s,2)