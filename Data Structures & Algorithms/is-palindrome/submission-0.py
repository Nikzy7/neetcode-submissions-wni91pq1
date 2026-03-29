class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_to_check = ""

        for ch in s:
            if ch.isalnum():
                s_to_check += ch.lower()

        len_to_parse = len(s_to_check) // 2

        right_ptr = len(s_to_check) - 1

        for left_ptr in range(0, len_to_parse):
            if s_to_check[left_ptr] != s_to_check[right_ptr]:
                return False

            right_ptr -= 1

        return True