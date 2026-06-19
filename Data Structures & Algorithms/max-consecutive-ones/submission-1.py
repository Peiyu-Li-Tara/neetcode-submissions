class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sum = 0
        tmp_sum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp_sum += 1
            else:
                if tmp_sum > max_sum:
                    max_sum = tmp_sum
                tmp_sum = 0
        return max_sum if tmp_sum < max_sum else tmp_sum

        