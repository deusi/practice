class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right, score = 0, len(tokens) - 1, 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            elif score > 0 and power < tokens[left] and left < right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return score