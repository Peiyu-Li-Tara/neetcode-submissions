class Solution:
    def mergeSort(self, row: List[int], target: int) -> bool:
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < row[mid]:
                r = mid - 1
            elif target > row[mid]:
                l = mid + 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for row in matrix:
            lower, upper = row[0], row[n - 1]
            if target == lower or target == upper:
                return True
            if target > lower and target < upper:
                return self.mergeSort(row, target)
        
        return False
                