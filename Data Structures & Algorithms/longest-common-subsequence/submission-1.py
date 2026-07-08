class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # R, C = len(text1), len(text2)
        # dp = [[0] * (C + 1) for _ in range(R + 1)]
        
        # for r in range(R - 1, -1, -1):
        #     for c in range(C - 1, -1, -1):
        #         if text1[r] == text2[c]:
        #             dp[r][c] = 1 + dp[r + 1][c + 1]
        #         else:
        #             dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        # return dp[0][0]

        cache = {}

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return cache[(i, j)]
        return dfs(0, 0)