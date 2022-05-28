# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        notCelebrity = set()
        def isCelebrity(num):
            for j in range(n):
                if j == num:
                    continue
                if not knows(j, num):
                    notCelebrity.add(num)
                    return False
                if knows(num, j):
                    notCelebrity.add(num)
                    return False
            return True
        
        for i in range(n - 1):
            if knows(i, i + 1):
                notCelebrity.add(i)
                continue
            if not knows(i + 1, i):
                notCelebrity.add(i + 1)
                continue
            if isCelebrity(i):
                return i
            
        if n - 1 not in notCelebrity and isCelebrity(n - 1):
                return n - 1    
        return -1