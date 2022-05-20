class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1]:
            return 0
        # create row and column for dp
        rowGrid = [obstacleGrid[0][i] for i in range(n)]
        colGrid = [obstacleGrid[i][0] for i in range(m)]
        
        # update row and column with values for dp
        rowGrid[0], colGrid[0] = 1, 1
        for i in range(1, n):
            if rowGrid[i] == 1:
                rowGrid[i] = 0
            else:
                rowGrid[i] = min(1, rowGrid[i - 1])
                
        for i in range(1, m):
            if colGrid[i] == 1:
                colGrid[i] = 0
            else:
                colGrid[i] = min(1, colGrid[i - 1])
        
        prev = 0
        for i in range(1, m):
            prev = colGrid[i]
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    rowGrid[j] = 0
                else:
                    rowGrid[j] = rowGrid[j] + prev
                prev = rowGrid[j]
                    
        return rowGrid[n - 1]
                    