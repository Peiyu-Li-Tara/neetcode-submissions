class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []

        # i is the index of the current element we visit in nums
        def backtrack(i):
            if i >= len(nums):
                ret.append(curr[:])
                return
            
            # if we include nums[i] in curr
            curr.append(nums[i])
            backtrack(i + 1)

            # if we are not include nums[i] in curr
            curr.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return ret
        