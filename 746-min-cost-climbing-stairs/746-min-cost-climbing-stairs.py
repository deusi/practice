class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2: return min(cost)
        cur, prev1, prev2 = 0, cost[1], cost[0]
        for i in range(2, len(cost)):
            cur = min(prev1, prev2) + cost[i]
            prev1, prev2 = cur, prev1
        return min(prev1, prev2)