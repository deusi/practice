class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIdx = {}
        for i, num in enumerate(nums):
            if target - num in numToIdx:
                return [numToIdx[target - num], i]
            numToIdx[num] = i
        return [-1, -1]