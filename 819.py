from collections import Counter
import heapq
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for i in "!?',;.":
            paragraph=paragraph.replace(i," ")

        paragraph = paragraph.lower()
        l1 = paragraph.split()
        c = Counter(l1)
        l = []
        for k,v in c.items():
            l.append((-v,k))
        heapq.heapify(l)
        while (len(l)>0):
            p = heapq.heappop(l)
            if p[1] not in banned:
                return p[1]

        return ""

if __name__ == "__main__":
    s = Solution()
    print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
    print(s.mostCommonWord("a, a, a, a, b,b,b,c, c",["a"]))