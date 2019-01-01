class Solution(object):
    def __init__(self):
        self.d = {}

    def is_solution(self, k,n,i, a):
        if n == 0:
            return True
        else:
            return False

    def process_solution(self, k,n,i,a):
        p = a[:]
        a = sorted(a, reverse=False)
        s = "".join([str(s) for s in a])
        self.d[s]= p


    def bt(self, data,n,i, a):

        if n < 0 :
            return

        if n==0:
            p = a[:]
            a = sorted(a, reverse=False)
            s = "".join([str(s) for s in a])
            self.d[s] = p
        else:
            c = data
            for j in range(len(c)):
                a.append(c[j])
                self.bt(data, n-c[j], i+1,a)
                a.pop()
        return

    def combinationSum(self, data, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        if n==0:
            return [[]]
        if n==1 and 1 in data:
            return [[1]]
        elif n ==1 and 1 not in data:
            return []

        a = []
        self.bt(data,n,0, a)

        return self.d.values()

if __name__ == "__main__":
    s = Solution()

    print(s.combinationSum([2,3,5],8))