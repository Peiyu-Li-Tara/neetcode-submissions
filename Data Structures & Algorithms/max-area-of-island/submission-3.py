class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return

        max_island = 0
        R, C = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r == R or c == C or grid[r][c] == 0 or (r, c) in visited:
                return 0 
            area = 1
            visited.add((r, c))
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area


        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_island = max(max_island, area)
        return max_island




