class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # R, C = len(obstacleGrid), len(obstacleGrid[0])
        # cache = [[-1] * C for _ in range(R)]
        
        # def dfs(r, c):
        #     if r >= R or c >= C:
        #         return 0
        #     if obstacleGrid[r][c] == 1:
        #         return 0
        #     if r == R - 1 and c == C - 1:
        #         return 1
        #     if cache[r][c] != -1:
        #         return cache[r][c]
        #     cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
        #     return cache[r][c]
        
        # dfs(0, 0)
        # return dfs(0, 0)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prev_row = [0] * n
        for i in range(m - 1, -1, -1):
            cur_row = [0] * n
            if obstacleGrid[i][n - 1] == 1:
                cur_row[n - 1] = 0
            else:
                cur_row[n - 1] = 1 if i == m - 1 else prev_row[n - 1]
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    cur_row[j] = 0
                else:
                    cur_row[j] = cur_row[j + 1] + prev_row[j]
            prev_row = cur_row
        return cur_row[0]