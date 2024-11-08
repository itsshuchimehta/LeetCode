class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMagazine = {}

        for l in magazine:
            if l in hashMagazine:
                hashMagazine[l] += 1
            else:
                hashMagazine[l] = 1

        for letter in ransomNote:
            if letter in hashMagazine and hashMagazine[letter] > 0:
                hashMagazine[letter] -= 1
            else:
                return False
        return True     