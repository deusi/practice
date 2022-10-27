class Solution:
    def knightDialer(self, n: int) -> int:
        jumps = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        @cache
        def dfs(num, upTo):
            if upTo == n:
                return 1
            ans = 0
            for cur in jumps[num]:
                ans += dfs(cur, upTo + 1)
            return ans
        
        answer = 0
        for i in range(0, 10):
            answer += dfs(i, 1)
            
        return answer % (10** 9 + 7)