class element:
    def __init__(self, i, v):
        self.v = i
        self.f = v


class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1

        l = []
        for v,f in d.items():
            e = element(v,f)
            l.append(e)

        l.sort(key=lambda x : x.f, reverse=True)
        #print(l)
        ans = []
        for i in range(k):
            ans.append(l[i].v)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.topKFrequent([1,1,1,2,2,3],2)