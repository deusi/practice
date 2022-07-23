class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        low = prices[0]
        for high in prices:
            low = min(low, high)
            maxProfit = max(maxProfit, high - low)
        return maxProfit