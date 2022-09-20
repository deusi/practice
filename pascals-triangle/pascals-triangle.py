class Solution:
    # Runtime Complexity: O(n^2) - since we need to generate previous rows to get to current one, i.e row 5 = 5 + 4 + 3 + 2 + 1
    # Space Complexity: O(n^2)
    # Time Taken: 17 m
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            newRow = [1 for _ in range(i + 1)]
            for j in range(i + 1):
                if j - 1 >= 0 and j < len(triangle[-1]):
                    newRow[j] = triangle[-1][j - 1] + triangle[-1][j]
            triangle.append(newRow)
        return triangle
        
        