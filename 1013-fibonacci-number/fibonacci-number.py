class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        p1 = self.fib(n-1)
        p2 = self.fib(n-2)

        return p1 + p2