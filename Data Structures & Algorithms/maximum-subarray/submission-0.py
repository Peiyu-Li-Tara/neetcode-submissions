class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = cur_sum

        for n in nums[1:]:
            cur_sum = max(cur_sum, 0)
            cur_sum += n
            max_sum = max(max_sum, cur_sum)
        
        return max_sum