class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set  = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            w = right - left + 1
            max_len = max(max_len, w)
        return max_len
        
        