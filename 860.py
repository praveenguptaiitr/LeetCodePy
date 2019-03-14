class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        d = {5:0, 10:0, 20:0}
        #ans = True
        for b in bills:
            if b == 5:
                d[5]=d[5]+1
                continue
            if b == 10:
                if d[5]>0:
                    d[5]=d[5]-1
                    d[10]=d[10]+1
                    continue
                else:
                    return False
            if b==20:
                if (d[10]>0 and d[5]>0):
                    d[10]=d[10]-1
                    d[5]=d[5]-1
                    d[20]=d[20]+1
                    continue
                elif  (d[5]>2):
                    d[5]=d[5]-3
                    continue
                else:
                    return False

        return True