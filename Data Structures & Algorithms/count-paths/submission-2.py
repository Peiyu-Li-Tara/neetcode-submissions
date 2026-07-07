class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # top down dp
        # cache = [[-1] * n for _ in range(m)]
        # def dfs(i, j):
        #     if i >= m or j >= n:
        #         return 0
        #     if i == m - 1 and j == n - 1:
        #         return 1
        #     if cache[i][j] != -1:
        #         return cache[i][j]
        #     cache[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
        #     return cache[i][j]
        # ret = dfs(0, 0)
        # return ret

        # bottom up
        prev_row = [0] * n
        for i in range(m - 1, -1, -1):
            cur_row = [0] * n
            cur_row[-1] = 1
            for j in range(n - 2, -1, -1):
                cur_row[j] = cur_row[j + 1] + prev_row[j]
            prev_row = cur_row
        return cur_row[0]