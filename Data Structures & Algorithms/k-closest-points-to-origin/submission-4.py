class Solution:
    # def getDist(self, point: List[int]) -> int:
    #     return math.sqrt(point[0] ** 2 + point[1] ** 2)

    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     # quick select
    #     ret = []

    #     def quickSelect(l, r):
    #         pivot, p = points[r], l
    #         for i in range(l, r):
    #             if self.getDist(points[i]) <= self.getDist(pivot):
    #                 points[i], points[p] = points[p], points[i]
    #                 p += 1
    #         points[r], points[p] = points[p], points[r]
    #         if p < k:
    #             quickSelect(l, p - 1)
    #         elif p > k:
    #             quickSelect(p + 1, r)
    #         else:
    #             for x in points[:p]:
    #                 ret.append(x)
    #             return
        
    #     quickSelect(0, len(points) - 1)
    #     return ret
    def kClosest(self, points, k):
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]
