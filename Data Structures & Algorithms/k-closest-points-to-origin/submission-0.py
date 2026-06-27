class Solution:
    def distance(self, point: List[int]):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
    
    def quickSortHelper(self, points, s, e):
        if e - s + 1 <= 1:
            return
        
        left = s
        pivot = points[e]

        for i in range(s, e):
            if self.distance(points[i]) < self.distance(pivot):
                tmp = points[left]
                points[left] = points[i] 
                points[i] = tmp
                left += 1
        
        points[e] = points[left]
        points[left] = pivot

        self.quickSortHelper(points, s, left - 1)
        self.quickSortHelper(points, left + 1, e)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSortHelper(points, 0, len(points) - 1)
        return points[:k]

        