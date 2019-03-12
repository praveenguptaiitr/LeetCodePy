import heapq
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        adj = [[] for i in range(N+1)]
        dist = [float("inf")]*(N+1)
        addedToTree = [0]*(N+1)
        for e in times:
            u,v,w = e[0],e[1],e[2]
            adj[u].append((v,w))

        src = K
        l = []

        dist[K]=0
        l.append((0,K))
        heapq.heapify(l)
        added = 0
        while len(l)!=0:
            d,u = heapq.heappop(l)
            if addedToTree[u]==1:
                continue
            addedToTree[u]=1
            added+=1

            for edge in adj[u]:
                v,w = edge[0],edge[1]
                if dist[v] > dist[u]+w:
                    dist[v]=dist[u]+w
                    heapq.heappush(l,(dist[v],v))

        if added == N:
            return max(dist[1:])
        else:
            return -1

if __name__ == "__main__":
    s = Solution()
    print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))