class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = 0, 0, 0
        L, R = nums1[: m], nums2
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                nums1[k] = L[i]
                i += 1
            else:
                nums1[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            nums1[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            nums1[k] = R[j]
            j += 1
            k += 1