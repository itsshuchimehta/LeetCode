

class Solution:
    """
Input: s = "3[a2[c]]"
Output: "accaccacc"


stack [("",3)]

c_s = accaccacc
last_string = "a"
repeat_num = 2

"""
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == "[":
                stack.append((current_string, k))
                current_string = ""
                k = 0
            elif char == "]":
                last_string, repeat_num = stack.pop()
                current_string = last_string + current_string * repeat_num
            else:
                current_string += char

        return current_string






























