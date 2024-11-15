class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return int(tokens[0])
        stack = []

        for i in tokens:
            if i in ["+", "-", "/", "*"]:
                first = stack.pop()
                second = stack.pop()
                if i == "+":
                    result = second + first
                    # ans = f"({ans} + {popped})"
                elif i == "*":             
                    result = second * first           
                    # ans = f"({ans} * {popped})"
                elif i == "/":
                    result = int(second / first)
                    # ans = f"({popped} // {ans})"
                elif i == "-":
                    result = second - first
                    # ans = f"({popped} - {ans})"
                
                stack.append(result)

            else:
                stack.append(int(i))
        
        return result