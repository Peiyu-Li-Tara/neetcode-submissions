class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Space complexity O(m)
        # i, j, k = 0, 0, 0
        # L = nums1[: m]
        # while i < len(L) and j < len(nums2):
        #     if L[i] <= nums2[j]:
        #         nums1[k] = L[i]
        #         i += 1
        #     else:
        #         nums1[k] = nums2[j]
        #         j += 1
        #     k += 1
        
        # while i < len(L):
        #     nums1[k] = L[i]
        #     i += 1
        #     k += 1
        # while j < len(nums2):
        #     nums1[k] = nums2[j]
        #     j += 1
        #     k += 1

        # Space complexity O(1)
        # Idea: We insert from right to left in nums1
        last = m + n - 1
        i, j = m - 1, n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1



