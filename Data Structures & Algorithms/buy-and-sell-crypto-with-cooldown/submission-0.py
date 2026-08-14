class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def buy(day, buying_allowed):
            if day >= n:
                return 0

            profit = 0

            if buying_allowed:
                should_buy = -prices[day] + (
                    buy(day + 1, False) if (day + 1, False) not in dp else dp[(day + 1, False)]
                )
                not_buy = 0 + (
                    buy(day + 1, True) if (day + 1, True) not in dp else dp[(day + 1, True)]
                )

                profit = max(should_buy, not_buy)

            else:
                not_sell = 0 + (
                    buy(day + 1, False) if (day + 1, False) not in dp else dp[(day + 1, False)]
                )
                sell = prices[day] + (
                    buy(day + 2, True) if (day + 2, True) not in dp else dp[(day + 2, True)]
                )  # because cooldown

                profit = max(sell, not_sell)

            dp[(day, buying_allowed)] = profit
            return profit

        return buy(0, True)
