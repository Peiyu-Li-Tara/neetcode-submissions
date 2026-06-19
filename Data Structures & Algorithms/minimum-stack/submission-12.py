class MinStack:

    def __init__(self):
        self.stack = []
        self.topIndex = -1
        self.decend = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.topIndex += 1
        newMin = min(val, self.decend[-1] if self.decend else val)
        self.decend.append(newMin)
        # print(self.stack, self.decend)
        

    def pop(self) -> None:
        popVal = self.stack.pop()
        self.topIndex -= 1
        self.decend.pop()
        

    def top(self) -> int:
        return self.stack[self.topIndex]
        

    def getMin(self) -> int:
        print(self.decend)
        return self.decend[-1]


        