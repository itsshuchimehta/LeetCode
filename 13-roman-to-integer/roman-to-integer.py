class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total_sum = 0
        i = 0
        n = len(s)

        while i < n:
            if i < n - 1 and roman_num[s[i]] < roman_num[s[i + 1]]:
                total_sum += roman_num[s[i + 1]] - roman_num[s[i]]
                i += 1
            else:
                total_sum += roman_num[s[i]]

            i += 1

        return total_sum
