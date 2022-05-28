class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        allNums, missingNum = 0,0
        for i in range(1, len(nums) + 1):
            allNums ^= i
        for num in nums:
            missingNum ^= num
        return missingNum ^ allNums