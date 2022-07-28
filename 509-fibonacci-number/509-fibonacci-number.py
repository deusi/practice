class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n), used to store the results of previous calls to fib
    @cache
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)