from bisect import bisect_left, bisect_right
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        startTime.sort()
        n = len(jobs)
        dp = [-1] * n 
        
        def dfs(cur_idx):
            if cur_idx >= n:
                return 0
            if dp[cur_idx] != -1:
                return dp[cur_idx]
            
            nxt_idx = bisect_left(startTime, jobs[cur_idx][1])
            dp[cur_idx] = max(dfs(cur_idx + 1), jobs[cur_idx][2] + dfs(nxt_idx))
            return dp[cur_idx]
        
        return dfs(0)