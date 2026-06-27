# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return
        
        left = s
        pivot = pairs[e]
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1
        
        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.quickSortHelper(pairs, s, left - 1)
        self.quickSortHelper(pairs, left + 1, e)
        
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s, e = 0, len(pairs) - 1
        self.quickSortHelper(pairs, s, e)
        return pairs

        
