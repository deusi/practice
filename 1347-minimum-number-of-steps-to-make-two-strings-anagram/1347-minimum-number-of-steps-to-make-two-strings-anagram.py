class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter = collections.Counter(s)
        for i in t:
            if i in counter and counter[i] > 0:
                counter[i] -= 1
        total = 0
        for val in counter.values():
            total += val
        return total