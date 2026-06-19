class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [] * self.capacity


    def get(self, i: int) -> int:
        print(i)
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        if i < 0 or i > self.capacity - 1:
            return
        else:
            if self.getSize() == 0:
                print(self.arr)
                self.arr.append(n)
            else:
                self.arr[i] = n
        print("after set: ", self.arr)


    def pushback(self, n: int) -> None:
        if len(self.arr) == self.capacity:
            self.resize()
            print("after resize: ", self.arr)
            self.arr.append(n)
        else:
            self.arr.append(n)
        print("after pushback: ", self.arr)


    def popback(self) -> int:
        return self.arr.pop()
 

    def resize(self) -> None:
        self.capacity *= 2
        newArr = [] * self.capacity
        for i in self.arr:
            newArr.append(i)
        self.arr = newArr
        print(self.arr)
            

    def getSize(self) -> int:
        return len(self.arr)
        
    
    def getCapacity(self) -> int:
        return self.capacity
