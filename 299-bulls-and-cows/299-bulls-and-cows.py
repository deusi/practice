class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sMap, gMap = collections.Counter(secret), collections.Counter(guess)
        iMap = {}
        for s in sMap:
            if s in gMap:
                iMap[s] = min(sMap[s], gMap[s])
        bulls, cows = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                iMap[s] -= 1
                bulls += 1
        cows = sum(iMap.values())
        return str(bulls) + 'A' + str(cows) + 'B'