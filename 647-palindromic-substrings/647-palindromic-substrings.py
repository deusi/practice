class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        # 1-letter string is a palindrome
        for i in range(n):
            dp[i][i] = True
            count += 1
         # find 2-letter palindromes   
        for i in range(1, n):
            if s[i] == s[i - 1]:
                dp[i - 1][i] = True
                count += 1
        # find n-letter palindromes based on n-1-lettered palindromes that were already found        
        for l in range(2, n):
            for i, j in zip(range(0, n - l), range(l, n)):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1
                    
        return count