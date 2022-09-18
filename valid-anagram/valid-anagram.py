class Solution:
    # Runtime Complexity: O(n) - n to create a counter and n to go through the second string
    # Space Complexity: O(n) - n to store the counter
    # Total Time: 5 m
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = collections.Counter(s)
        for letter in t:
            if letter not in counter or counter[letter] <= 0:
                return False
            counter[letter] -= 1
        return True