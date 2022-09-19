class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        verDir, horDir = 0, 1
        curX, curY = 0, 0
        result = []
        while left < right and top < bottom:
            result.append(matrix[curX][curY])
            if curX + verDir >= bottom:
                verDir = 0
                horDir = -1
                right -= 1
            if curX + verDir < top:
                verDir = 0
                horDir = 1
                left += 1
            if curY + horDir >= right:
                verDir = 1
                horDir = 0
                top += 1
            if curY + horDir < left:
                verDir = -1
                horDir = 0
                bottom -= 1
            curX += verDir
            curY += horDir
        return result