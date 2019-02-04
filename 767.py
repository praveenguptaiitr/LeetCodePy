from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S):
        ans = ""
        heap = []
        c = Counter(S)
        for k, v in c.items():
            heapq.heappush(heap, (-v, k))
        p_a, p_b = 0, ''
        while heap:
            a, b = heapq.heappop(heap)
            ans += b
            if p_a < 0:
                heapq.heappush(heap, (p_a, p_b))
            a += 1
            p_a, p_b = a, b

        if len(ans) != len(S): return ""
        return ans