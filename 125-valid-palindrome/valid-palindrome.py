class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len(original)
        if n == 0:
            return True
        return self.helper(original, 0, n)
    
    def helper(self, s, i, n):
        
        if i >= n//2:
            return True
        if s[i] != s[n-i-1]:
            return False
        return self.helper(s, i+1, n)    