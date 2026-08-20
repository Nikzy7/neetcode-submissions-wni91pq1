class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        def r(seen):
            if len(seen) == N:
                return []

            answer = []

            for num in nums:
                if num not in seen:
                    seen.add(num)
                    recur = r(seen)
                    if len(recur) == 0:
                        answer.append([num])
                    else:
                        for x in recur:
                            answer.append([num] + x)
                    seen.remove(num)

            return answer

        return r(set())