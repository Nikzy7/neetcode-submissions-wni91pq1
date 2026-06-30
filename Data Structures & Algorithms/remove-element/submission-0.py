class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valsRemoved = 0
        left = 0
        right = 0 

        while left < len(nums):
            if nums[left] == val:
                right = left+1
                while right < len(nums):
                    if nums[right] != val:
                        break
                    right += 1
                if right < len(nums):
                    nums[left], nums[right] = nums[right], nums[left]
                    valsRemoved += 1
                else:
                    break
            else:
                valsRemoved += 1
            left += 1

        return valsRemoved