from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, A, S):
        res, sm  = 0, 0
        sums = defaultdict(int)
        for a in A:
            sm += a
            res += sums[sm - S] + (sm == S)
            sums[sm] += 1
        return res