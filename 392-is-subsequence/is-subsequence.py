class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if s == '': return True
        if s == t: return True
        if S > T: return False

        j = 0
        for i in range(T):
            
            if t[i] == s[j]:
                j+=1

            if j == S:
                return True
            
        return False





