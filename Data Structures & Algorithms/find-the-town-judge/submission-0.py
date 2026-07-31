class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        citizens = [0 for _ in range(n+1)]

        for citizen in trust:
            citizens[citizen[0]] -= 1
            citizens[citizen[1]] += 1

        for i in range(1, n + 1):
            if citizens[i] == n - 1:
                return i

        return -1