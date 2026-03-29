class Solution:
    def isPalindrome(self, s: str) -> bool:
        right_ptr = len(s) - 1

        for left_ptr in range(0, len(s)):
            if not s[left_ptr].isalnum():
                continue

            while not s[right_ptr].isalnum():
                right_ptr -= 1

            if left_ptr >= right_ptr:
                break

            if s[left_ptr].lower() != s[right_ptr].lower():
                return False

            right_ptr -= 1

        return True