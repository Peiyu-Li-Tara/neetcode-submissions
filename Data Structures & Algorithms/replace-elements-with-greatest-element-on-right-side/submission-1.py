class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse iteration
        # new max = max(oldmax, arr[i])
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax, curr)
        return arr


        

        