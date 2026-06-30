class MinHeap:
    
    def __init__(self):
        self.minHeap = [0]

    def push(self, val: int) -> None:
        self.minHeap.append(val)

        i = len(self.minHeap) - 1
        while i > 1 and self.minHeap[i // 2] > self.minHeap[i]:
            tmp = self.minHeap[i // 2]
            self.minHeap[i // 2] = self.minHeap[i]
            self.minHeap[i] = tmp
            i = i // 2


    def pop(self) -> int:
        if len(self.minHeap) == 1:
            return -1
        if len(self.minHeap) == 2:
            return self.minHeap.pop()
        
        i = 1
        ret = self.minHeap[i]
        self.minHeap[i] = self.minHeap.pop()
        while i * 2 < len(self.minHeap):
            if (2 * i + 1 < len(self.minHeap) and 
                self.minHeap[2 * i + 1] < self.minHeap[2 * i] and 
                self.minHeap[i] > self.minHeap[2 * i + 1]):
                # Swap right child
                tmp = self.minHeap[i]
                self.minHeap[i] = self.minHeap[2 * i + 1]
                self.minHeap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.minHeap[i] > self.minHeap[i * 2]:
                # Swap left child
                tmp = self.minHeap[i]
                self.minHeap[i] = self.minHeap[2 * i]
                self.minHeap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return ret
        

    def top(self) -> int:
        if len(self.minHeap) == 1:
            return -1
        return self.minHeap[1]
        

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            return
        nums.append(nums[0])
        self.minHeap = nums
        cur = (len(self.minHeap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
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
            cur -= 1
            