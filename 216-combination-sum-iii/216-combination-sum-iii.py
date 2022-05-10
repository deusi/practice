class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        if k >= n:
            return result
        
        def backtracking(curNum, startNum, numList):
            if curNum > n or len(numList) > k:
                return
            elif len(numList) == k and curNum == n:
                result.append(numList[:])
            else:
                for i in range(startNum, 10):
                    numList.append(i)
                    backtracking(curNum + i, i + 1, numList)
                    numList.pop()
                    
        backtracking(0, 1, [])
        return result