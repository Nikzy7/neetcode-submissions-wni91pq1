class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        dp = {}

        def recursion(currentAmount):
            if currentAmount > amount:
                return INF

            if currentAmount == amount:
                return 0

            if currentAmount in dp:
                return dp[currentAmount]

            min_coins = INF

            for coin in coins:
                res = recursion(currentAmount + coin)
                if res != INF:
                    min_coins = min(min_coins, 1 + res)

            dp[currentAmount] = min_coins
            return dp[currentAmount]

        answer = recursion(0)
        return answer if answer != INF else -1
