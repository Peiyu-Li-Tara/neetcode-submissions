class Solution:
    def getDist(self, point: List[int]) -> int:
        return math.sqrt(point[0] ** 2 + point[1] ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Heap
        minHeap = [(self.getDist(point), point) for point in points]
        heapq.heapify(minHeap)
        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(minHeap)[1])
        return ret
        
        