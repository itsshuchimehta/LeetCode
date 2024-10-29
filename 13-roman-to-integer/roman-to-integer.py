class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            'I' : 1,
            'V' : 5,
            'X' :10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total_sum = 0
        i = 0
        while i < len(s):
            
            if s[i] == 'I' and i <= len(s) - 2 and s[i + 1] in ['V', 'X']:
                if s[i + 1] == 'V':
                    total_sum += 4
                    i += 1
                elif s[i + 1] == 'X':
                    total_sum += 9
                    i += 1
            
            elif s[i] == 'X' and i <= len(s) - 2 and s[i + 1] in ['L', 'C']:
                if s[i + 1] == 'L':
                    total_sum += 40
                    i += 1
                elif s[i + 1] == 'C':
                    total_sum += 90
                    i += 1
        
            elif s[i] == 'C' and i <= len(s) - 2 and s[i + 1] in ['D', 'M']:
                if s[i + 1] == 'D':
                    total_sum += 400
                    i += 1
                elif s[i + 1] == 'M':
                    total_sum += 900
                    i += 1
            else:
                total_sum += roman_num[s[i]]
            
            i += 1

        return total_sum
