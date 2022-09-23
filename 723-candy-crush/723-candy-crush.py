class Solution:
    # Runtime Complexity: O(m * n * k), where k is the number of times we need to iterate before the board is the same
    # m*n for both findCandies and propagateZeroes
    # Space Complexity: O(m*n), since we would have to store all the indicies in the set in the worst case
    # Total Time: more than I'm comfortable admitting
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def findCandies():
            m, n = len(board), len(board[0])
            found = False
            crash = set()
            for i in range(m):
                count = 1
                candidates = set()
                candidates.add((i, 0))
                for j in range(1, n):
                    if board[i][j] != board[i][j - 1] or board[i][j] == 0:
                        if count >= 3:
                            crash |= candidates
                        candidates = set()
                        count = 0
                    count += 1
                    candidates.add((i,j))
                if count >= 3:
                    crash |= candidates
                    
            for i in range(n):
                count = 1
                candidates = set()
                candidates.add((0, i))
                for j in range(1, m):
                    if board[j][i] != board[j-1][i] or board[j][i] == 0:
                        if count >= 3:
                            crash |= candidates
                        candidates = set()
                        count = 0
                    count += 1
                    candidates.add((j,i))
                if count >= 3:
                    crash |= candidates
                    
            if len(crash):
                found = True
                for r, c in crash:
                    board[r][c] = 0        
                
            return found        
            
         
        def propagateZeroes():
            m, n = len(board), len(board[0])
            for i in range(n):
                zeroPtr, elsePtr = m - 1, m - 1
                while elsePtr > -1:
                    board[zeroPtr][i], board[elsePtr][i] = board[elsePtr][i], board[zeroPtr][i]
                    if board[zeroPtr][i] != 0:
                        zeroPtr -= 1
                    elsePtr -= 1
        
        while findCandies():
            propagateZeroes()
                
        return board
            