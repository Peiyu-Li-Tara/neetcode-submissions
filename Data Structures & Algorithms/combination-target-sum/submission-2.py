class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        
        def backtrack(i, cur, total):
            if total == target:
                ret.append(cur[:])
                return
            
            if i >= len(nums) or total > target:
                # print(cur)
                return
            
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])

            cur.pop()
            backtrack(i + 1, cur, total)
            return
        
        backtrack(0, [], 0)
        return ret
