class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}
        for i, n in enumerate(nums):
            if target - n in nMap:
                return [nMap[target - n], i]
            nMap[n] = i