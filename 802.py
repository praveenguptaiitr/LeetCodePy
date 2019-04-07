class Solution(object):
    def eventualSafeNodes(self, graph):
        def dfs(node, path, visited, cycle):
            if visited[node] == 1 or node in cycle:
                cycle |= set(path)
            elif visited[node] == 0:
                path.append(node)
                visited[node] = 1
                for child in graph[node]:
                    dfs(child, path, visited, cycle)
                visited[node] = 2
                path.pop()

        cycle, visited = set(), [0] * len(graph)
        for node in range(len(graph)):
            dfs(node, [], visited, cycle)
        return sorted(set(range(len(graph))) - cycle)

if __name__ == "__main__":
    s = Solution()
    print(s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
