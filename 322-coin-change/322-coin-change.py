class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        
        mem = {}
        def dp(rem, usedCoins):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in mem:
                return mem[rem]
            
            minVal = inf
            for coin in coins:
                res = dp(rem - coin, usedCoins + 1)
                if res >= 0 and res < minVal:
                    minVal = res + 1
                    
            mem[rem] = -1 if minVal == inf else minVal
            return mem[rem]
            
        return dp(amount, 0)