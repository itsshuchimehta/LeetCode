from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 7:
            return 0
        
        target = "balloon"

        ch_counter = defaultdict(int)

        for ch in text:
            if ch in target:
                ch_counter[ch] += 1
        
        if any(c not in ch_counter for c in target):
            return 0
        else:
            return min(ch_counter['b'], ch_counter['a'], ch_counter['l']//2, ch_counter['o']//2, ch_counter['n']) 
        
