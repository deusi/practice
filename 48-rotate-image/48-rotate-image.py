class Solution:
    # Runtime Complexity: (n^2) to reverse the columns and switch rows with columns
    # Space Complexity: O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. Reverse the columns
        for i in range(len(matrix) // 2):
            for j in range(len(matrix[0])):
                matrix[i][j], matrix[len(matrix) - i - 1][j] = matrix[len(matrix) - i - 1][j], matrix[i][j]
        # 2. Switch rows with columns
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]