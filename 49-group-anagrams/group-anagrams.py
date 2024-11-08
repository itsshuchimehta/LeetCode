from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26      # Array to count each letter in the string
            for c in s:
                count[ord(c) - ord('a')] += 1 # Count characters
             
            key = tuple(count) # Use the count as a tuple as the key
            anagrams_dict[key].append(s)
        
        return list(anagrams_dict.values())