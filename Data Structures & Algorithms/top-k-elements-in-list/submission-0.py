class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        heap = []
        for n, cnt in freq.items():
            heapq.heappush(heap, (cnt, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]