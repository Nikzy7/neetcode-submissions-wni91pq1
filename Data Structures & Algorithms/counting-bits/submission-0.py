class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []

        def count(n) -> int:
            ones = 0

            for _ in range(10):
                if n & 1 == 1:
                    ones += 1
                n = n >> 1

            return ones

        for n in range(n + 1):
            answer.append(count(n))

        return answer
