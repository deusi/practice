class Solution:
    # Runtime Complexity: O(2^n)
    # Space Complexity: O(2^n)
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        def listToInt(nums):
            ans = nums[0]
            for i in range(1, len(nums)):
                ans *= 10
                ans += nums[i]
            return ans
        
        # could optimize to only go through candidate numbers, but too lazy now (rc still stays the same, improve constant)
        def bt(nums):
            if len(nums) == n:
                result.append(listToInt(nums))
                return
            start = 0
            if sum(nums) == 0:
                start = 1
            for i in range(start, 10):
                if len(nums) == 0 or abs(i - nums[-1]) == k:
                    nums.append(i)
                    bt(nums)
                    nums.pop()
            return
        
        nums = []
        bt(nums)
        return result