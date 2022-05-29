class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxProd = 0
        for i in range(len(words)):
            letters = set(words[i])
            for j in range(i + 1, len(words)):
                unique = True
                for l in words[j]:
                    if l in letters:
                        unique = False
                        break
                if unique:
                    maxProd = max(maxProd, len(words[i]) * len(words[j]))
        return maxProd