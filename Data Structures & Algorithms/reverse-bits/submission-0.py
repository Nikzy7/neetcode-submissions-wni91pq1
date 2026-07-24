class Solution:
    def reverseBits(self, n: int) -> int:
        ans = ""

        for x in range(32):
            ans += str(n&1)
            n = n>>1

        return int(ans,2)