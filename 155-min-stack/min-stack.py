class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.MinStack:
            self.MinStack.append(val)
        elif self.MinStack[-1] < val:
            self.MinStack.append(self.MinStack[-1])
        else:
            self.MinStack.append(val)

    def pop(self) -> None:
        self.stack.pop()    
        self.MinStack.pop()  
    
    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.MinStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()