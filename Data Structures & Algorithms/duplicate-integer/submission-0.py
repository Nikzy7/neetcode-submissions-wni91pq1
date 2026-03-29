class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = dict()
        for n in nums:
            if freq_map.get(n,False):
                return True
            else:
                freq_map[n] = True

        return False

        