class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZero = 0
        for right in range(len(nums)):
            nonZero = max(nonZero, right)
            if nums[right] == 0:
                while nonZero < len(nums) and nums[nonZero] == 0:
                    nonZero += 1
                if nonZero >= len(nums):
                    break
                nums[right], nums[nonZero] = nums[nonZero], nums[right]
                nonZero += 1
        return nums