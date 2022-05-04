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
        # needed to iterate over every unique number in nums
        keys = list(numDict.keys())
        i, n = 0, len(keys)
        while i < n:
            target = k - keys[i]
            # check if there exists a number such that target + keys[i] = k
            if target in numDict and (target != keys[i] and numDict[keys[i]] >= 1 and numDict[target] >= 1) or (target == keys[i] and numDict[target] >= 2):
                numDict[keys[i]] -= 1
                numDict[target] -= 1
                maxOp += 1
            else:
                # if no, use the next key number in the next iteration
                i += 1
        return maxOp