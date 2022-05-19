from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ranks = {}
        for i in range(n):
            ranks[i] = None
        graph = defaultdict(list)
        critical = set()
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            critical.add((min(u, v), max(u, v)))
        def dfs(node, rank):
            if ranks[node]:
                return ranks[node]
            ranks[node] = rank
            minRank = rank + 1
            for neighbour in graph[node]:
                if ranks[neighbour] and ranks[neighbour] == rank - 1:
                    continue
                neighbourRank = dfs(neighbour, rank + 1)
                if neighbourRank <= rank:
                    ncNode = (min(node, neighbour), max(node, neighbour))
                    critical.remove(ncNode)
                    minRank = min(minRank, neighbourRank)
            return minRank
        dfs(0,0)
        result = []
        while critical:
            u, v = critical.pop()
            result.append([u,v])
        return result