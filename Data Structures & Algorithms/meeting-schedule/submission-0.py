"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        heap = []
        intervals.sort(key=lambda i: i.start)

        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
            elif heap[0] <= interval.start:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
            else:
                return False
        
        if len(heap) > 1:
            return False
        return True