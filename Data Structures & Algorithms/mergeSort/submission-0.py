# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSortHelper(self, pairs, s, e):
            if (e - s) + 1 <= 1:
                return pairs
            
            m = (s + e) // 2

            self.mergeSortHelper(pairs, s, m)
            self.mergeSortHelper(pairs, m + 1, e)
            self.merge(pairs, s, m, e)

            return pairs
    
    def merge(self, pairs, s, m, e):
            L, R = pairs[s: m + 1], pairs[m + 1: e + 1]
            i, j, k = 0, 0, s
            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    pairs[k] = L[i]
                    i += 1
                else:
                    pairs[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                pairs[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                pairs[k] = R[j]
                j += 1
                k += 1

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
