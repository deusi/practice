class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        changed.sort()
        counter = collections.Counter(changed)
        original = []
        for c in changed:
            if 2*c in counter and counter[c] > 0 and counter[2*c] > 0:
                if c == 0 and counter[c] == 1:
                    continue 
                original.append(c)
                counter[c] -= 1
                counter[2*c] -= 1
        return original if n == 2 * len(original) else []