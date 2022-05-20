from collections import defaultdict

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid) - 1, len(grid[0]) - 1
        visited = set()
        uniqueCount = 0
        uniqueIslands = defaultdict(list)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def checkIfUnique(island):
            nonlocal uniqueCount
            iLength = len(island)
            if iLength not in uniqueIslands:
                uniqueCount += 1
                uniqueIslands[iLength].append(island)
                return
            for curIsland in uniqueIslands[iLength]:
                if curIsland == island:
                    return
            uniqueCount += 1
            uniqueIslands[iLength].append(island)
            return
        
        def dfs(row, col, origRow, origCol, island):
            for first, second in directions:
                nRow, nCol = row + first, col + second
                if nRow < 0 or nRow > m or nCol < 0 or nCol > n or grid[nRow][nCol] == 0 or (nRow, nCol) in visited:
                    continue
                island.append((origRow - nRow, origCol - nCol))
                visited.add((nRow, nCol))
                dfs(nRow, nCol, origRow, origCol, island)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                candidateIsland = []
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    candidateIsland.append((0, 0))
                    dfs(i, j, i, j, candidateIsland)
                    checkIfUnique(candidateIsland)
        
        return uniqueCount