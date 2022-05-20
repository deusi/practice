class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0 
        
        m,n = len(matrix) - 1, len(matrix[0]) - 1
        directions = [(1, 0), (-1, 0), (0, 1), (0 ,-1)]
        maxPath = 0
        
        @cache
        def dfs(row, col):
            curPath = 0
            for first, second in directions:
                nRow, nCol = row + first, col + second
                if nRow < 0 or nRow > m or nCol < 0 or nCol > n or matrix[nRow][nCol] <= matrix[row][col]:
                    continue
                curPath = max(curPath, dfs(nRow, nCol))
            curPath += 1
            return curPath
        
        for i in range(m + 1):
            for j in range(n + 1):
                maxPath = max(maxPath, dfs(i, j))
                
        return maxPath