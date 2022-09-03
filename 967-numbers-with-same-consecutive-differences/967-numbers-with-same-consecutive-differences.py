class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        def bt(nums):
            if len(nums) == n:
                st = [str(i) for i in nums]
                result.append(int(''.join(st)))
                return
            start = 0
            if len(nums) == 0 or sum(nums) == 0:
                start = 1
            for i in range(start, 10):
                if len(nums) == 0:
                    nums.append(i)
                    bt(nums)
                    nums.pop()
                elif abs(i - nums[-1]) == k:
                    nums.append(i)
                    bt(nums)
                    nums.pop()
            return
        nums = []
        bt(nums)
        return result