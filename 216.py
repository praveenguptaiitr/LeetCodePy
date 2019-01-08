class Solution(object):
    def __init__(self):
        self.d = {}

    # def is_solution(self, k,n,i, a):
    #     if n == 0 and len(a)==k:
    #         return True
    #     else:
    #         return False
    #
    # def process_solution(self, k,n,i,a):
    #     p = a[:]
    #     a = sorted(a, reverse=False)
    #     s = "".join([str(s) for s in a])
    #     self.d[s]= p


    def bt(self, k,n,i, a):

        if n < 0 :
            return

        if n!=0 and len(a)>=k:
            return

        if n==0 and k==len(a):
            p = a[:]
            a = sorted(a, reverse=False)
            s = "".join([str(s) for s in a])
            self.d[s] = p
        else:
            #l1 = [1,2,3,4,5,6,7,8,9]
            s = set(a)
            c = []
            for i in range(1,10):
                if i not in s:
                    c.append(i)
            #c = [i for i in l1 if i not in a]
            for j in range(len(c)):
                a.append(c[j])
                self.bt(k, n-c[j], i+1,a)
                a.pop()
        return

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        if n==0:
            return [[]]
        if n==1 and k==1:
            return [[1]]
        elif n ==1 and k!=1:
            return []

        a = []
        self.bt(k,n,0, a)

        return self.d.values()

if __name__ == "__main__":
    s = Solution()

    print(s.combinationSum3(3,9))