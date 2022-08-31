class Solution:
    # Runtime Complexity: O(m*n), since we will go through each element in the worst case
    # Space Complexity: O(m*n), since each element in an island might have water flow to p&a
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = collections.deque()
        atlantic = collections.deque()
        for i in range(len(heights[0])):
            pacific.append((0, i))
            atlantic.append((len(heights) - 1, i))
        for i in range(1, len(heights)):
            pacific.append((i, 0))
            atlantic.append((i - 1, len(heights[0]) - 1))
        pacificSet = set(pacific)
        atlanticSet = set(atlantic)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while pacific:
            r, c = pacific.popleft()
            for d1, d2 in dirs:
                nR, nC = r+d1, c+d2
                if nR < 0 or nR >= len(heights) or nC < 0 or nC >= len(heights[0]) or heights[nR][nC] < heights[r][c] or (nR, nC) in pacificSet:
                    continue
                pacific.append((nR, nC))
                pacificSet.add((nR, nC))
        while atlantic:
            r, c = atlantic.popleft()
            for d1, d2 in dirs:
                nR, nC = r+d1, c+d2
                if nR < 0 or nR >= len(heights) or nC < 0 or nC >= len(heights[0]) or heights[nR][nC] < heights[r][c] or (nR, nC) in atlanticSet:
                    continue
                atlantic.append((nR, nC))
                atlanticSet.add((nR, nC))
        return list(pacificSet.intersection(atlanticSet))