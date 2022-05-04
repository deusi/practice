class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        maxOp = 0
        keys = list(numDict.keys())
        i, n = 0, len(keys)
        while i < n:
            target = k - keys[i]
            if target in numDict:
                if (target != keys[i] and numDict[keys[i]] >= 1 and numDict[target] >= 1) or (target == keys[i] and numDict[target] >= 2):
                    numDict[keys[i]] -= 1
                    numDict[target] -= 1
                    maxOp += 1
                else:
                    i += 1
            else:
                i += 1
        return maxOp