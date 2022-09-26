class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(idx, target):
            counter = set()
            for j in range(idx, len(nums)):
                if target - nums[j] in counter:
                    result.add((nums[idx-1], target - nums[j], nums[j]))
                counter.add(nums[j])
                
        result = set()
        nums.sort()
        for i in range(len(nums) - 2):
            twoSum(i + 1, -nums[i])
            if i > 0 and nums[i - 1] == nums[i] == nums[i + 1]:
                continue
            if nums[i] > 0:
                break
                
        return result