# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, 
# starting with word1. If a string 
# is longer than the other, append the additional letters 
# onto the end of the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge =[]
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            merge.append(word1[i])
            merge.append(word2[j])
            i += 1
            j += 1

        while i < len(word1):
            merge.append(word1[i])
            i += 1
            
        while j < len(word2):
            merge.append(word2[j])
            j += 1
            
        return ''.join(merge)