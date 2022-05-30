class Solution:
    # had lots of troubles coming up with this solution and looked up a chunk of it
    # try it again
    def divide(self, dividend: int, divisor: int) -> int:
        negatives, q = 0, 0
        MAX_INT, MIN_INT, HALF_MIN = 2147483647, -2147483648, -1073741824
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        if dividend > 0:
            dividend = -dividend
            negatives += 1
        if divisor > 0:
            divisor = -divisor
            negatives += 1
            
        i = -1
        powers, doubles = [], []
        while divisor >= dividend:
            powers.append(divisor)
            doubles.append(i)
            if divisor < HALF_MIN:
                break
            i += i
            divisor += divisor
            
        for i in range(len(powers) - 1, -1 ,-1):
            if powers[i] >= dividend:
                q += doubles[i]
                dividend -= powers[i]
            
        return q if negatives == 1 else -q