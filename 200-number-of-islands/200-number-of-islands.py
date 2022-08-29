class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        islandCount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    islandCount += 1
                    grid[r][c] = '2'
                    queue = collections.deque([(r, c)])
                    while queue:
                        cR, cC = queue.popleft()
                        for d1, d2 in dirs:
                            if cR + d1 >= 0 and cR + d1 < len(grid) and cC + d2 >= 0 and cC + d2 < len(grid[0]) and grid[cR + d1][cC + d2] == '1':
                                grid[cR + d1][cC + d2] = '2'
                                queue.append((cR + d1, cC + d2))
        return islandCount