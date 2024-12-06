class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        res, sol = [], []
        n= len(digits)

        letter_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz'}

        def backtrack(i):
            if i == n:
                res.append("".join(sol))
                return
            
            for letter in letter_map[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()
            
        backtrack(0)
        return res

        # TC:O(n * 4**n) or O(4**n)
        # SC:O(N)
        