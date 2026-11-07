class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min:
            if value < self.min[-1]:
                self.min.append(value)
            else:
                self.min.append(self.min[-1])
        else:
            self.min.append(value)
            
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
    
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min[-1]
        

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()