class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {e: 1 for e in arr}
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    candidate = arr[i] // arr[j]
                    if candidate in dp:
                        dp[arr[i]] += (dp[arr[j]] * dp[candidate]) % MOD
        return sum(dp.values()) % MOD