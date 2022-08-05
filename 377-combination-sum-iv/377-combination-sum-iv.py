class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def bt(curSum):
            if curSum == target:
                return 1
            cur = 0
            for num in nums:
                if curSum + num > target:
                    continue
                cur += bt(curSum + num)
            return cur
        return bt(0)