class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [0]
        self.k = k
        self.cnt = 0
        for i in nums:
            self.addHelper(i)
        

    def add(self, val: int) -> int:
        self.addHelper(val)
        return self.minHeap[1]
    
    def addHelper(self, val: int) -> None:
        self.minHeap.append(val)
        i = len(self.minHeap) - 1
        while i > 1 and self.minHeap[i] < self.minHeap[i // 2]:
            tmp = self.minHeap[i]
            self.minHeap[i] = self.minHeap[i // 2]
            self.minHeap[i // 2] = tmp
            i = i // 2
        
        self.cnt += 1
        if self.cnt == self.k + 1:
            self.popHelper()
            self.cnt -= 1
        
        print(self.minHeap)
    
    def popHelper(self):
        if len(self.minHeap) == 1:
            return
        if len(self.minHeap) == 2:
            self.minHeap.pop()
            return
        
        i = 1
        self.minHeap[i] = self.minHeap.pop()
        
        while 2 * i < len(self.minHeap):
            if (2 * i + 1 < len(self.minHeap) and 
            self.minHeap[2 * i + 1] < self.minHeap[2 * i] and 
            self.minHeap[i] > self.minHeap[2 * i + 1]):
                # Swap right child
                tmp = self.minHeap[i]
                self.minHeap[i] = self.minHeap[2 * i + 1]
                self.minHeap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.minHeap[i] > self.minHeap[2 * i]:
                # Swap left child
                tmp = self.minHeap[i]
                self.minHeap[i] = self.minHeap[2 * i]
                self.minHeap[2 * i] = tmp
                i = 2 * i
            else:
                break
                




                