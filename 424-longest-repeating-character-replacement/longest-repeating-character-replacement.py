class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        L = 0
        counts = [0] * 26
        
        for R in range(len(s)):
            counts[ord(s[R]) - 65] += 1
            while (R-L+1) - max(counts) > k:
                counts[ord(s[L]) - 65] -= 1
                L += 1            
            w = (R - L) + 1
            longest = max(longest, w)
        return longest
