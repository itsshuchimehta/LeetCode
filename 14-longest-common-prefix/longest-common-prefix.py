class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num_of_str = len(strs)

        if num_of_str == 1:
            return strs[0]
        
        result = []
        j = 0
        for ch in strs[0]:
            i = 1
            while i  < num_of_str and j < len(strs[i]):
                if ch == strs[i][j]:
                    i+=1          
                else:
                    return "".join(result)
                
                if i == num_of_str:
                    result.append(ch)
                    j+=1

        return "".join(result)