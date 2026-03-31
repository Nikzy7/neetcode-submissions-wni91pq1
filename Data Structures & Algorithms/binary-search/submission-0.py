class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            # in case of java or c++ if left or right is 2^31 then adding them both
            # can overflow the integer limit, so one more way to calculate mid is
            # left + ((right - left) // 2)
            # in python its not a problem
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1

        return -1