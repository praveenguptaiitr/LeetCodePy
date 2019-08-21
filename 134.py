class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1


        start = 0
        tot = 0
        for i in range(len(gas)):
            tot += gas[i]-cost[i]
            if tot < 0:
                start = i+1
                tot = 0

        return start



if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))