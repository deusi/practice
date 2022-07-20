class Solution:
    # Runtime Complexity: O(m), where m = len(t)
	# Space Complexity: O(1) - no extra space used
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        cur = 0
        for char in t:
            if s[cur] == char:
                cur += 1
                # no need to keep iterating if the full subsequence matched
                if cur == len(s):
                    return True
        return cur == len(s)