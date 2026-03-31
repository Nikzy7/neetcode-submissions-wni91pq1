class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        sorted_items_by_value = sorted(freq_dict.items(), key=lambda item: item[1])
        sorted_items_by_value.reverse()
        sorted_freq_dict = dict(sorted_items_by_value)

        to_return = []

        for key in sorted_freq_dict.keys():
            to_return.append(key)
            if len(to_return) == k:
                break

        return to_return