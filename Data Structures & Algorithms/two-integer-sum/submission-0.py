class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        presence = dict()

        for i in range(len(nums)):
            presence[nums[i]] = presence.get(nums[i], []) + [i]

        for left_num, left_num_indices in presence.items():
            right_num = target - left_num

            right_num_indices = presence.get(right_num, [])

            if len(right_num_indices) != 0:
                for l in left_num_indices:
                    for r in right_num_indices:
                        if l != r:
                            return [l, r]

        return [None, None]