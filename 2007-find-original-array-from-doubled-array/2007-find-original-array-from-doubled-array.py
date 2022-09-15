class Solution:
    # Runtime Complexity: O(n log n)
    # Space ComplexityL O(n)
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        changed.sort()
        counter = collections.Counter(changed)
        original = []
        for c in changed:
            if counter[c] > 0:
                counter[c] -= 1
                if 2*c in counter and counter[2*c] > 0:
                    original.append(c)
                    counter[2*c] -= 1
                else:
                    return []
        return original