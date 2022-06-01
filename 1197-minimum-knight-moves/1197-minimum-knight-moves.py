from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0:
            return 0
        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        queue = deque([(0,0)])
        visited = set()
        visited.add((0,0))
        length = 0
        while queue:
            length += 1
            for _ in range(len(queue)):
                curX, curY = queue.popleft()
                for move in moves:
                    nX, nY = curX + move[0], curY + move[1]
                    if nX == x and nY == y:
                        return length
                    if (nX, nY) not in visited:
                        visited.add((nX, nY))
                        queue.append((nX, nY))
        return length