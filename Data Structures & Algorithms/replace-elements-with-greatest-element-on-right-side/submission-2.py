class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]
            arr[i] = curr_max
            if val > curr_max:
                curr_max = val
        return arr