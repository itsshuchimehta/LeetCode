class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = [0] * 26
        L = 0
        R = len(s1) - 1

        for c in s1:
            counts[ord(c) - ord('a')] += 1

        while R < len(s2):
            temp = [0] * 26
            for ch in range(L,R+1):
                temp[ord(s2[ch]) - ord('a')] += 1
            
            # check 
            if temp == counts:
                return True
            
            L += 1
            R += 1
        return False
