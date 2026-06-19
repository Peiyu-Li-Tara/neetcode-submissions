class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # brute force
        # count = 0
        # cur = 0
        # if not nums:
        #     return 0
        # while cur <= len(nums) - 1 and nums[cur] >= 0:
        #     if nums[cur] == val:
        #         for i in range(cur + 1, len(nums)):
        #             nums[i - 1] = nums[i]
        #         nums[len(nums) - 1] = -1
        #         count += 1
        #         print(nums)
        #     else:
        #         cur += 1
        # return len(nums) - count

        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k