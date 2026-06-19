class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force
        for i in range(len(arr) - 1):
            cur_max = arr[i + 1]
            for j in range(i + 1, len(arr)):
                if arr[j] >= cur_max:
                    cur_max = arr[j]
                    arr[i] = arr[j]
        arr[len(arr) - 1] = -1
        return arr

        