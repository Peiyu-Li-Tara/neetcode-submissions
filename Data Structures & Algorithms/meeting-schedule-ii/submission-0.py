"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        intervals.sort(key=lambda i: i.start)

        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
            elif heap[0] <= interval.start:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
            else:
                heapq.heappush(heap, interval.end)
        
        return len(heap)