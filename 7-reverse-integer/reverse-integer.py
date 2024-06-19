class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        result = 0
        sign = -1 if x < 0 else 1
        x=abs(x)

        while x > 0:
            lastDigit = x % 10
            result = (result * 10) + lastDigit
            x = x // 10

            if result > INT_MAX:
                return 0
        result *= sign

        if result < INT_MIN or result > INT_MAX:
            return 0

        return result