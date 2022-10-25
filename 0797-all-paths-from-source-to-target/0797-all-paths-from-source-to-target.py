class Solution:
    # Runtime Complexity: O(2^N * n)
    # Space Complexity: O(n)
    # Total Time: 8 m
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        result = []
        def bt(node, path):
            for c in graph[node]:
                path.append(c)
                if c == n:
                    result.append(path[:])
                else:
                    bt(c, path)
                path.pop()
        bt(0, [0])
        return result
                