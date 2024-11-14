class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        open_br_stack = []   
        
        for i in s:
            if i in ["(", "{", "["]:
                open_br_stack.append(i)
            
            elif open_br_stack and i in [")","]","}"]:
                    end = open_br_stack.pop()
                    if (i == ")" and end != "(") or (i == "]" and end != "[") or (i == "}" and end != "{"):
                        return False
            else:
                return False
        if open_br_stack:
            return False        
    
        return True
            
            
