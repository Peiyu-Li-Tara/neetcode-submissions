class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[-1] * C for _ in range(R)]
        
        def dfs(r, c):
            if r >= R or c >= C:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == R - 1 and c == C - 1:
                return 1
            if cache[r][c] != -1:
                return cache[r][c]
            cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[r][c]
        
        dfs(0, 0)
        return dfs(0, 0)