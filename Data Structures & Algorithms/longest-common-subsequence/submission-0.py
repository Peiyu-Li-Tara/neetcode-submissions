class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R, C = len(text1), len(text2)
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        return dp[0][0]