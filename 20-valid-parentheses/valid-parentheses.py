class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {']':'[', ')':'(', '}':'{'}
        open_br_stack = []
        for c in s:
            if c not in hashmap:
                open_br_stack.append(c)
            else:
                if not open_br_stack:
                    return False
                else:
                    popped = open_br_stack.pop()
                    if popped != hashmap[c]:
                        return False
        return not open_br_stack
            
            
