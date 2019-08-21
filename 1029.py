class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        c = sorted(costs, key = lambda x: x[0]-x[1])
        return sum([cost[0] for cost in c[:len(c)//2]]) + sum([cost[1] for cost in c[len(c)//2:]])


if __name__ == "__main__":
    s = Solution()
    print(s.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))