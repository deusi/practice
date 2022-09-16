# Technical debt
class Solution:
    # Runtime Complexity: O(m^2)
    # Space Complexity: (m)
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m, n = len(multipliers), len(nums)
        dp = [0 for _ in range(m + 1)]
        for op in range(m - 1, -1, -1):
            next_row = dp.copy()
            for left in range(op, -1, -1):
                dp[left] = max(multipliers[op] * nums[left] + next_row[left + 1],
                               multipliers[op] * nums[n - 1 - (op - left)] + next_row[left])
        return dp[0]