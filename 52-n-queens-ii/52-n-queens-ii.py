class Solution:
    # Time Complexity: O(N!)
    # Space Complexity: O(1)
    def totalNQueens(self, n: int) -> int:
        sols = 0
        columns, diagonal, antidiagonal = set(), set(), set()
        def bt(row):
            nonlocal sols
            if row == n:
                sols += 1
            for col in range(n):
                if col not in columns and row - col not in diagonal and row + col not in antidiagonal:
                    columns.add(col)
                    diagonal.add(row - col)
                    antidiagonal.add(row + col)
                    bt(row + 1)
                    columns.remove(col)
                    diagonal.remove(row - col)
                    antidiagonal.remove(row + col)
        bt(0)
        return sols