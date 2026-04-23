class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = []
    def push(self, val: int) -> None:
        self.stack.append(val)   
        if self.stack2:
            self.stack2.append(min(val, self.stack2[-1]))
        else:
            self.stack2.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.stack2.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack2[-1]
        
