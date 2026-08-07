class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOver = 1

        ptr = len(digits)-1

        while carryOver != 0:
            if ptr == -1:
                digits = [carryOver] + digits
                carryOver = 0
            else:
                digits[ptr] += carryOver
                if digits[ptr] > 9:
                    digits[ptr] = 0
                else:
                    carryOver = 0
                ptr-=1

        return digits