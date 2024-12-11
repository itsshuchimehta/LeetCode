from heapq import heappush, heappop
from collections import Counter


    
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count frequency of each character
        freq_map = Counter(s)
        # Create a max-heap based on character frequency
        max_heap = []
        for char, freq in freq_map.items():
            heappush(max_heap, (-freq, char))
        
        # Reconstruct the string
        prev_char, prev_freq = None, 0
        result = []
        
        while max_heap:
            freq, char = heappop(max_heap)  # Get the most frequent character
            result.append(char)  # Add to result
            # Push the previous character back if its frequency is non-zero
            if prev_freq < 0:
                heappush(max_heap, (prev_freq, prev_char))
            # Update previous character and frequency
            prev_char, prev_freq = char, freq + 1
        
        # If the result length matches the input, we succeeded
        return ''.join(result) if len(result) == len(s) else ""