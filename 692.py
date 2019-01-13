#from functools import  cmp_to_key
import heapq
# def compare_key_new(a, b):
#     if a[0] < b[0]:
#         return -1
#     elif a[0]>b[0]:
#         return 1
#     else:
#         return a[1]>b[1]

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        for w in words:
            d[w]=d.get(w,0)+1
        l = []
        for k1,v1 in d.items():
            l.append((-v1,k1))

        heapq.heapify(l)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(l)[1])
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent(["aaa","aa","a"], 1))
    print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4))
    print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2))