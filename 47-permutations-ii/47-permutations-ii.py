from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        counter = Counter(nums)
        result = []
        def backtracking(perm):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            for num in counter:
                if counter[num] <= 0:
                    continue
                counter[num] -= 1
                perm.append(num)
                backtracking(perm)
                counter[num] += 1
                perm.pop()
                
        backtracking([])
        return result