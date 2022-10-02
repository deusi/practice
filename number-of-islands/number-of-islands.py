class Solution:
    # Runtime Complexity: O(m*n) to go over every num in a grid
    # Space Complexity: O(max(m, n)) to store queue
    # Total Time: 9 m
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        dirs = [(0, 1), (1, 0), (0, -1),(-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    queue.append((i, j))
                    while queue:
                        r, c = queue.popleft()
                        for d1, d2 in dirs:
                            nR, nC = r + d1, c + d2
                            if nR < 0 or nC < 0 or nR >= m or nC >= n:
                                continue
                            if grid[nR][nC] == '0':
                                continue
                            grid[nR][nC] = '0'
                            queue.append((nR, nC))
        return islands
                    