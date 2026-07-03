class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or r == R or c == C or (r, c) in visit or grid[r][c] == 1:
                return 0
            if r == R - 1 and c == C - 1:
                return 1
            visit.add((r, c))
            count = 0
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            visit.remove((r, c))
            return count
        
        return dfs(0, 0)