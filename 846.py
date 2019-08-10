from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, W):
        count = Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m+W):
                v = count.get(k,None)
                if v== None:
                    return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
    print(s.isNStraightHand([1,2,3,4,5], 4))
