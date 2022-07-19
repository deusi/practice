class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum, pivot = 0, sum(nums), 0
        while pivot < len(nums):
            rightSum -= nums[pivot]
            if leftSum == rightSum:
                return pivot
            leftSum += nums[pivot]
            pivot += 1
        return -1