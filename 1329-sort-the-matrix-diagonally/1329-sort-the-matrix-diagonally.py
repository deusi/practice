class Solution:
    # Runtime Complexity: O(m*n log min(m, n)) to go through matrix and sort each diagonal
    # Space Complexity: O(min(m,n)) to store a sorted array
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for j in range(len(mat[0])):
            sortedDiagonal = []
            for i in range(len(mat)):
                if j+i >= len(mat[0]):
                    break
                sortedDiagonal.append(mat[i][j+i])
            sortedDiagonal.sort()
            for i in range(0, len(mat)):
                if j+i >= len(mat[0]):
                    break
                mat[i][j+i] = sortedDiagonal[i]
        for i in range(1, len(mat)):
            sortedDiagonal = []
            for j in range(len(mat[0])):
                if j+i >= len(mat):
                    break
                sortedDiagonal.append(mat[i+j][j])
            sortedDiagonal.sort()
            for j in range(len(mat[0])):
                if j+i >= len(mat):
                    break
                mat[i+j][j] = sortedDiagonal[j]
        return mat
                