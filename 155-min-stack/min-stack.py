class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []
        self.newMin = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.MinStack: 
            if self.MinStack[-1] < val:
                self.MinStack.append(self.newMin)
            else:
                self.newMin = val
                self.MinStack.append(val)
        else:
            self.newMin = val
            self.MinStack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()    
        if self.MinStack:
            self.MinStack.pop()
        if self.MinStack:
            self.newMin = self.MinStack[-1]   
    

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]        

    def getMin(self) -> int:
        if self.MinStack:
            return self.MinStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()