class Solution:
    def minSwaps(self, data: List[int]) -> int:
        totalOnes = sum(data)
        if totalOnes == len(data):
            return 0
        curOnes = sum(data[0: totalOnes])
        minSwap = totalOnes - curOnes
        left = 0
        for right in range(totalOnes, len(data)):
            curOnes += data[right]
            curOnes -= data[left]
            left += 1
            minSwap = min(minSwap, totalOnes - curOnes)
        return minSwap