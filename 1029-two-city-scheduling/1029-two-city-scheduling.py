class Solution:
    # Runtime Complexity: O(n log n) for sorting
    # Space Complexity: O(n) for sorting algorithm
    # Total Time: 8 m
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])
        return sum(x for x,_ in costs[:n]) + sum(y for _, y in costs[n:])