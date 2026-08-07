class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def get_squared_digits(n):
            to_return = 0

            while n > 0:
                to_return += (n % 10) ** 2
                n = n // 10

            return to_return

        while n != 1:
            n = get_squared_digits(n)

            if n in seen:
                return False

            seen.add(n)

        return True
