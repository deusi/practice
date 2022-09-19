class Solution:
    # Runtime Complexity: O(m*n) to go over every element of the matrix
    # Space Complexity: O(1) - excluding resulting array, we only use boundaries
    # Total Time: 31 m
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        verDir, horDir = 0, 1
        curX, curY = 0, 0
        dirs = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        result = []
        while left < right and top < bottom:
            result.append(matrix[curX][curY])
            if curX + verDir >= bottom:
                verDir, horDir = dirs[2]
                right -= 1
            if curX + verDir < top:
                verDir, horDir = dirs[0]
                left += 1
            if curY + horDir >= right:
                verDir, horDir = dirs[1]
                top += 1
            if curY + horDir < left:
                verDir, horDir = dirs[3]
                bottom -= 1
            curX += verDir
            curY += horDir
        return result