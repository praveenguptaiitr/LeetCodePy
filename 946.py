class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        l = []
        idx = 0
        for e in pushed:
            l.append(e)
            while len(l)>0 and l[-1]==popped[idx]:
                l.pop()
                idx+=1

        return len(l)==0