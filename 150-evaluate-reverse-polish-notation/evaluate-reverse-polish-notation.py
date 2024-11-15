class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+", "-", "/", "*"]:
                first = stack.pop()
                second = stack.pop()
                if i == "+":
                    result = second + first
                elif i == "*":             
                    result = second * first           
                elif i == "/":
                    result = int(second / first)
                elif i == "-":
                    result = second - first
            
                stack.append(result)
            else:
                stack.append(int(i))
        
        return stack[0]