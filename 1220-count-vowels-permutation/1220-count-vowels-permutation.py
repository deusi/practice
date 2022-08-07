class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def countVowelPermutation(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        @cache
        def bt(idx, curN):
            if curN > n:
                return 1
            num = 0
            vowel = vowels[idx]
            if vowel == 'a':
                num += bt(1, curN + 1)
            elif vowel == 'e':
                num += bt(0, curN + 1) + bt(2, curN + 1)
            elif vowel == 'i':
                num += bt(0, curN + 1) + bt(1, curN + 1) + bt(3, curN + 1) + bt(4, curN + 1)
            elif vowel == 'o':
                num += bt(2, curN + 1) + bt(4, curN + 1)
            else: 
                num += bt(0, curN + 1)
            return num % (10**9 + 7)
        ans = 0
        for v in range(len(vowels)):
            ans += bt(v, 2)
        return ans % (10**9 + 7)
                              