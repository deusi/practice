class Solution:
    # Runtime Complexity: O(len(n)): O(log n) to get to len(n) and O(len(n)) to compare
    # Space Complexity: O(len(n)) for dictionaries
    def reorderedPowerOf2(self, n: int) -> bool:
        sN = str(n)
        nDict = collections.Counter(sN)
        pow2 = 1
        pow2S = str(pow2)
        while len(pow2S) <= len(sN):
            if len(pow2S) == len(sN):
                # could be optimized for one dict instead by subtracting and adding elements in a separate function
                pow2Dict = collections.Counter(pow2S)
                if pow2Dict == nDict:
                    return True
            pow2 *= 2
            pow2S = str(pow2)
        return False