from collections import defaultdict
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alph = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for w in words:
            ans = ""
            for c in w:
                ans = ans + alph[ord(c)-97]
            s.add(ans)
        return len(s)

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves =  moves.lower()
        h = defaultdict(int)
        for c in moves:
            h[c]= h.get(c,0)+1
        return (h['l'] == h['r']) and (h['u']==h['d'])


if __name__ == "__main__":
    s = Solution()
    #print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
    print(s.judgeCircle("LDRRLRUULR"))