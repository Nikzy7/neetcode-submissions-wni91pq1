class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## using moore voting algorithm
        candidate = -1
        count = 0

        for n in nums:
            if count == 0:
                candidate = n

            if n == candidate:
                count+=1
            else:
                count-=1

        return candidate