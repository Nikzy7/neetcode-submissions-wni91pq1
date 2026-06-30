class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0

        right = 0
        count = 0

        while right<len(nums):
            if nums[right] == 1:
                count += 1
            else:
                maxCount = max(maxCount,count)
                count = 0
            
            right += 1

        maxCount = max(maxCount,count)

        return maxCount


        