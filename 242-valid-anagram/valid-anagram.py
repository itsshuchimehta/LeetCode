from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = Counter(s) 
        freq_t = Counter(t) 

        return freq_s == freq_t