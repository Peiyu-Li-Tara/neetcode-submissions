class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down dp
        cache = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if cache[i][j] != -1:
                return cache[i][j]
            cache[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return cache[i][j]
        ret = dfs(0, 0)
        return ret