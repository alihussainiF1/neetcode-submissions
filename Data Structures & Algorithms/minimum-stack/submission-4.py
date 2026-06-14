class MinStack:

    def __init__(self):
        self.k=[]
        self.min_val = []

    def push(self, val: int) -> None:
        self.k.append(val)
        if self.min_val:
            if val <= self.min_val[-1]:
                self.min_val.append(val)
        else:
            self.min_val.append(val)
        

    def pop(self) -> None:
        if self.k:
            s=self.k.pop()
        if s == self.min_val[-1]:
            self.min_val.pop()

    def top(self) -> int:
        return self.k[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
