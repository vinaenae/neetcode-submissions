class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = val
        if self.min:
            min_val = min(self.min[-1], val)
        self.min.append(min_val) 

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
            
    def top(self) -> int:
        return self.stack[-1]  
        
    def getMin(self) -> int:
        return self.min[-1]
        
