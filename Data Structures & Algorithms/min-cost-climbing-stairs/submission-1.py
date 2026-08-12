class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}

        def recursion(n):
            if n >= len(cost):
                dp[n] = 0
                return 0

            jump_1 = cost[n] + (recursion(n + 1) if (n + 1) not in dp else dp[n + 1])
            jump_2 = cost[n] + (recursion(n + 2) if (n + 2) not in dp else dp[n + 2])
            dp[n] = min(jump_1, jump_2)

            return dp[n]

        return min(recursion(0), recursion(1))
