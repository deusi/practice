class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minArr = [None for _ in range(len(nums))]
        minArr[0] = nums[0]
        # create an array with 'i's for each j and k
        for i in range(1, len(nums)):
            minArr[i] = min(minArr[i - 1], nums[i])
        # store candidates for k
        stack = []
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= minArr[j]:
                continue
            while stack and stack[-1] <= minArr[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False