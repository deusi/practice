class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bt(i, j, cur, visited):
            if len(word) - 1 == cur and word[cur] == board[i][j]:
                return True
            if word[cur] != board[i][j]:
                return False
            exists = False
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d1, d2 in dirs:
                r, c = i + d1, j + d2
                if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in visited:
                    continue
                visited.add((r, c))
                exists = exists or bt(r, c, cur+1, visited)
                if exists:
                    return exists
                visited.remove((r, c))
            return exists
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if bt(i, j, 0, set([(i, j)])):
                    return True
                
        return False