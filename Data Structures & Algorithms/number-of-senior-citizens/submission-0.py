class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for person in details:
            if int(person[-4:-2]) > 60:
                count += 1

        return count
