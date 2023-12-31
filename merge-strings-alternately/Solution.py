class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_len = len(word1)
        w2_len = len(word2)
        result = ''

        if w1_len == w2_len:
            for i in range(w1_len):
                result += word1[i] + word2[i]
        elif w1_len > w2_len:
            for i in range(w2_len):
                result += word1[i] + word2[i]
            for i in range(w2_len, w1_len ):
                result += word1[i]
        elif w1_len < w2_len:
            for i in range(w1_len):
                result += word1[i] + word2[i]
            for i in range(w1_len, w2_len):
               
                result += word2[i]
        return result
