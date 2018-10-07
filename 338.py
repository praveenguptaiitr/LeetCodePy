class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]

        l = [0]*(num+1)
        l[0]=0
        l[1]=1
        x=2
        for i in range(2,num+1):
            if(i&(i-1)==0):
                x=i
            l[i]=1+l[i-x]

        return l

if __name__ == '__main__':
    s = Solution()
    print(s.countBits(10))