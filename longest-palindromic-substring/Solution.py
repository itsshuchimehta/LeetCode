class Solution:
    def longestPalindrome(self, s: str) -> str:
        rslt = {}
        if len(s) <= 1:
            return s
        else:
            reverse_string = s[::-1]

            if s == reverse_string :
                return s
            else:
                pl_str = ''
                for i in range(len(s)): 
                    if i+1 < len(s):
                        pl_str += str(s[i])
                        if s[i] == s[0] and i != 0 and pl_str == pl_str[::-1]:
                            rslt[len(pl_str)] = pl_str
    
                for i in range(len(s)):        
                    for j in range(i+1,len(s)):
                        if s[i] == s[j]:
                            pl_str = str(s[i])+str(s[j])
                            rslt[len(pl_str)] = pl_str
                        elif j + 1 < len(s) and s[i] == s[j + 1] :
                            pl_str = str(s[i])+str(s[j])+str(s[j+1])
                            
                            rslt[len(pl_str)] = pl_str
                
                        elif len(rslt) == 0:
                            rslt[1] = s[i]
                        else:
                            break

                for i in range(len(s)):                     
                    index_no = self.find_next_matching_element(s,i)
                    if index_no != None:
                        pl_str = ''
                        for j in range(i,index_no + 1):
                            pl_str += str(s[j])
                            if j == index_no and pl_str == pl_str[::-1]:
                                rslt[len(pl_str)] = pl_str
                                print(pl_str)
            
            max_len = rslt[max(rslt, key=lambda k: (k, rslt[k]))]
        return max_len

    def find_next_matching_element(self, string, i):
    # Check if the index is within the valid range
        if i < 0 or i >= len(string) - 1:
            return None  # Invalid index or already at the end of the string

        target_element = string[i]

        # Iterate starting from i + 1
        for j in range(i + 1, len(string)):
            if string[j] == target_element:
                return j  # Return the matching element

        return None  # No matching element found
