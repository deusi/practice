from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        if grid[0][0] == 1 or grid[n][n] == 1:
            return -1
        
        finalCoords = [n, n]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        queue = deque([[0, 0]])
        grid[0][0] = 1
        
        while queue:
            first, second = queue.popleft()
            if first == finalCoords[0] and second == finalCoords[1]:
                return grid[first][second]
            for i in range(len(directions)):
                newFirst, newSecond = first + directions[i][0], second + directions[i][1]
                nextCoord = [newFirst, newSecond]
                if newFirst > n or newFirst < 0 or newSecond > n or newSecond < 0 or grid[newFirst][newSecond] != 0:
                    continue
                grid[newFirst][newSecond] = grid[first][second] + 1
                queue.append(nextCoord)
        return -1