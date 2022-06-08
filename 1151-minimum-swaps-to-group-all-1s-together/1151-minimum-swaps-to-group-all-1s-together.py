class Solution:
    # Time Complexity: O(n), since we count number of 1s once and use the sliding window to go through the list
    # Space Complexity: O(1), since we only keep track of number of 1s in any given window
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