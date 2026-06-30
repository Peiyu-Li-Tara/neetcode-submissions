class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            # print(stones)
            stone1, stone2 = heapq.heappop_max(stones), heapq.heappop_max(stones)
            heapq.heappush_max(stones, max(0, abs(stone1 - stone2)))
        return stones[0]