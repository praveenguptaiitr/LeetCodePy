class Solution(object):

    def __init__(self):
        self.ans = []

    def is_solution(self):
        pass

    def process_solution(self, arr):
        #print(arr)
        p = arr[:]
        self.ans.append(p)

    def construct_candidates(self, i , N, arr):
        c = []
        p = arr[:i]
        for j in range(1,N+1):
            if (j%i == 0) or (i%j ==0):
                if j not in p:
                    c.append(j)
        return c

    def bt(self, data, k, arr, N):
        if k == N+1:
            self.process_solution(arr)
        else:
            c = self.construct_candidates(k, N, arr)
            for i in range(len(c)):
                arr[k]= c[i]
                self.bt(data, k+1, arr, N)


    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        data = [ i for i in range(1,N+1)]
        arr = [0]*(N+1)
        self.bt(data,1, arr, N)
        return len(self.ans)


if __name__ == "__main__":
    s = Solution()
    print(s.countArrangement(2))