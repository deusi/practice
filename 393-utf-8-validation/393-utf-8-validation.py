class Solution:
    # Runtime Complexity: (n)
    # Space Complexity: O(1)
    def validUtf8(self, data: List[int]) -> bool:
        bits = 0
        fmask = 1 << 6
        for d in data:
            mask = 1 << 7
            if bits == 0:
                while d > 0 and d & mask:
                    bits += 1
                    mask = mask >> 1
                    
                if bits == 0:
                    continue
                    
                if bits > 4 or bits == 1:
                    return False
                
            else:
                if not (d & mask and not (d & fmask)):
                    return False
            bits -= 1
        return bits == 0