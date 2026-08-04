class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for st in strs:
            count = [0 for _ in range(26)]

            for ch in st:
                count[ord(ch) - ord("a")] += 1

            res[tuple(count)].append(st)

        return list(res.values())