class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return ""
        dupCount = [[-1, -1]]
        for c in s:
            if c == dupCount[-1][0]:
                dupCount[-1][1] += 1
                if dupCount[-1][1] == k:
                    dupCount.pop()
            else:
                dupCount.append([c,1])
        result = []
        for dc in dupCount[1:]:
            result.append(dc[0] * dc[1])
        return "".join(result)