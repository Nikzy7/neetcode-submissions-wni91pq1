class Solution:
    def rob_1(self, nums: List[int]) -> int:
        dp = dict()

        def rob_recursion(n):
            if n >= len(nums):
                return 0

            next_to_next = nums[n] + (rob_recursion(n + 2) if (n + 2) not in dp else dp[n + 2])
            next_to_next_next = nums[n] + (rob_recursion(n + 3) if (n + 3) not in dp else dp[n + 3])

            dp[n] = max(next_to_next, next_to_next_next)

            return dp[n]

        return max(rob_recursion(0), rob_recursion(1))

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_1(nums[: len(nums) - 1]), self.rob_1(nums[1:]))
