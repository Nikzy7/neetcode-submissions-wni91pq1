class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        checkEven = False

        for x in range(len(nums)):
            if x == 0:
                checkEven = nums[x] % 2 != 0  # check for next turn
                continue

            if checkEven:
                if nums[x] % 2 != 0:
                    return False
            else:
                if nums[x] % 2 == 0:
                    return False

            checkEven = not (checkEven)

        return True
