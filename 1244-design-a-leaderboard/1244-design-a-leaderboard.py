# Total Time: 9 m
class Leaderboard:

    def __init__(self):
        self.scores = {}

    # Runtime, Space: O(1)
    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    # Runtime: O(nlogk)
    # Space O(n)
    def top(self, K: int) -> int:
        return sum(heapq.nlargest(K, self.scores.values()))
    
    # Runtime, Space: O(1)
    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)