class Solution:
    def climbStairs(self, n: int) -> int:
        dp = dict()

        def recursion(n):
            if n == 0 or n == 1:
                dp[n] = 1
                return 1

            left = dp.get(n - 1) if (n - 1) in dp else recursion(n - 1)
            right = dp.get(n - 2) if (n - 2) in dp else recursion(n - 2)

            dp[n] = left + right
            return dp[n]

        return recursion(n)