class Solution:
    # Runtime Complexity: O(m*n) to run through the entire grid
    # Space Complexity: O(m), for dp array
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        dp = [1 for _ in range(m)]
        for _ in range(n - 1):
            for j in range(1, m):
                dp[j] += dp[j - 1]
        return dp[-1]