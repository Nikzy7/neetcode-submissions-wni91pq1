class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]

        def travel(i, j):
            if i == 0 and j == 0:
                dp[i][j] = 1
                return 1
            if i < 0 or j < 0:
                return 0

            up = travel(i - 1, j) if dp[i - 1][j] == -1 else dp[i - 1][j]
            left = travel(i, j - 1) if dp[i][j-1] == -1 else dp[i][j-1]

            dp[i][j] = up + left

            return dp[i][j]

        return travel(m - 1, n - 1)