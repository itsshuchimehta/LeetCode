class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMagazine = {}

        for l in magazine:
            if l in hashMagazine:
                hashMagazine[l] += 1
            else:
                hashMagazine[l] = 1

        for letter in ransomNote:
            if letter not in hashMagazine:
                return False
            elif hashMagazine[letter] == 1:
                del hashMagazine[letter]
            else:
                hashMagazine[letter] -= 1
    
        return True     