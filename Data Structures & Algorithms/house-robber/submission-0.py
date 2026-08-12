class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = dict()

        def rob(n):
            if n >= len(nums):
                return 0

            next_to_next = nums[n] + (rob(n+2) if (n+2) not in dp else dp[n+2])
            next_to_next_next = nums[n] + (rob(n+3)if (n+3) not in dp else dp[n+3])

            dp[n] = max(next_to_next,next_to_next_next)

            return dp[n]

        return max(rob(0),rob(1))