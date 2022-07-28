class Solution:
    # Runtime Complexity: O(m*n) - because of nested for loop
    # Space Complexity: O(m*n), when queue deals with one hugh island
    def numIslands(self, grid: List[List[str]]) -> int:
        iCount = 0
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        queue = collections.deque()
        # O(m*n), but it would only happen once (one big island), hence overall numIslands would also be m*n
        # O(m*n)
        def visitIsland(row, col):
            grid[row][col] = '2'
            queue.append([row, col])
            while queue:
                r, c = queue.popleft()
                for d1, d2 in directions:
                    nR, nC = r+d1, c+d2
                    if nR >= len(grid) or nC >= len(grid[0]) or nR < 0 or nC < 0 or grid[nR][nC] != '1':
                        continue
                    grid[nR][nC] = '2'
                    queue.append([nR, nC])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    iCount += 1
                    visitIsland(i, j)
        return iCount