class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n

        for x in range(len(nums)+1):
            res = res ^ x

        return res
