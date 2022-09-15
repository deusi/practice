class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        counter = collections.Counter(changed)
        original = []
        for c in changed:
            if c in counter and c+c in counter:
                if c+c == 0 and counter[c+c] == 1:
                    continue
                original.append(c)
                counter[c+c] -= 1
                if counter[c+c] == 0:
                    del counter[c+c]
                if c in counter:
                    counter[c] -= 1
                    if counter[c] == 0:
                        del counter[c]
        if len(changed) == 2 * len(original):
            return original
        return []