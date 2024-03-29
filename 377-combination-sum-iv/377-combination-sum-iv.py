class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n) - due to recursion stack
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def bt(curSum):
            if curSum == 0:
                return 1
            cur = 0
            for num in nums:
                if curSum - num < 0:
                    continue
                cur += bt(curSum - num)
            return cur
        return bt(target)