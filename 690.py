class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id):
        emap = {e.id:e for e in employees}
        return self.dfs(id,emap)

    def dfs(self, id, emap):
        e = emap.get(id,None)
        if e is None:
            return 0
        ans = e.importance
        if e.subordinates is None:
            return ans

        for s in e.subordinates:
            ans+=self.dfs(s,emap)

        return ans
