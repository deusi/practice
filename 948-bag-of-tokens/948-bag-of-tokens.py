class Solution:
    # Time Complexity: O(n log n) - n log n to sort and n for two pointer solution
    # Space Complexity: O(1), no extra space used
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right, score = 0, len(tokens) - 1, 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            elif score > 0 and left < right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return score