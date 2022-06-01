class Solution:
    # Runtime Complexity: O(n), since we are going through each number in the array
    # Space Complexity: O(1), since we are modifying array in-place
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
            
        return nums