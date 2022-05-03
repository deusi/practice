class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
            left += 1
        if left == len(nums) - 1:
            return 0
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        if right == 0:
            return len(nums)
        subMin, subMax = inf, -inf
        for i in range(left, right + 1):
            subMin, subMax = min(subMin, nums[i]), max(subMax, nums[i])
        while left > 0:
            if subMin >= nums[left - 1]:
                break
            left -= 1
        while right < len(nums) - 1:
            if subMax <= nums[right + 1]:
                break
            right += 1
        return right - left + 1