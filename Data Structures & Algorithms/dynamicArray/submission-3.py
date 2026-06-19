class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        print("after set: ", self.arr, "size: ", self.size, "capacity: ", self.capacity)
        

    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
        if self.size == 0:
            self.set(0, n)
        else:
            self.set(self.size, n)
        self.size += 1
        print("after pushback: ", self.arr, "size: ", self.size, "capacity: ", self.capacity)
       

    def popback(self) -> int:
        ret = self.arr[self.size - 1]
        self.arr[self.size - 1] = 0
        self.size -= 1
        print("after popback: ", self.arr, "size: ", self.size, "capacity: ", self.capacity)
        return ret 

    def resize(self) -> None:
        self.capacity *= 2
        newArr = [0] * self.capacity
        for i in range(0, self.size):
            newArr[i] = self.arr[i]
        self.arr = newArr
        print("after resize: ", self.arr, "size: ", self.size, "capacity: ", self.capacity)
        

    def getSize(self) -> int:
        print("get size: ", self.size)
        return self.size
        
    
    def getCapacity(self) -> int:
        print("get capacity: ", self.capacity)
        return self.capacity
