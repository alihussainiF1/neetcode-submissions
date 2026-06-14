class MinStack:

    def __init__(self):
        
        self.min_stack=[]
        self.stack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)


    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
        else:
            return -1
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1 
        
