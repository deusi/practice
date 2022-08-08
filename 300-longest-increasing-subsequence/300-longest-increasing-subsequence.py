class Solution:
    # Runtime Complexity: O(n^2)
    # Space Complexity: O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxSeq, dp = 1, [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxSeq = max(maxSeq, dp[i])
        return maxSeq