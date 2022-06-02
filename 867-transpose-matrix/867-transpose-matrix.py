class Solution:
    # Time Complexity: O(m * n), where m is the number of rows and n is the number of cols in the matrix
    # Space Complexity: O(m * n), since we recreate a matrix
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        tMatrix = []
        for i in range(len(matrix[0])):
            tRow = []
            for j in range(len(matrix)):
                tRow.append(matrix[j][i])
            tMatrix.append(tRow)
        return tMatrix