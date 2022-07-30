class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        alphabet = [0 for _ in range(26)]
        longest, left, aSum = 0, 0, 0
        for right in range(len(s)):
            alphabet[ord(s[right]) - 65] += 1
            aSum += 1
            if aSum - max(alphabet) > k:
                alphabet[ord(s[left]) - 65] -= 1
                aSum -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest