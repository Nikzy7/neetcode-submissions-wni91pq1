class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def recursion(string):
            if len(string) == 0:
                return []
            
            if len(string) == 1:
                return list(combinations[string])

            answer = []

            for ch in combinations[string[0]]:
                to_add = [ch + x for x in recursion(string[1:])]
                answer += (to_add)

            return answer

        return recursion(digits)
