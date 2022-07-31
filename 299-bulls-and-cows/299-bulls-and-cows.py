class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        iMap = collections.Counter(secret) & collections.Counter(guess)
        bulls, cows = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                iMap[secret[i]] -= 1
                bulls += 1
        cows = sum(iMap.values())
        return str(bulls) + 'A' + str(cows) + 'B'