class Solution:
    def isValid(self, s: str) -> bool:
        def is_left(ch):
            return ch == "[" or ch == "{" or ch == "("

        def is_right(ch):
            return ch == "]" or ch == "}" or ch == ")"

        def are_pair(left, right):
            if (
                (left == "(" and right == ")")
                or (left == "{" and right == "}")
                or (left == "[" and right == "]")
            ):
                return True

            return False

        stack = []

        for ch in s:
            if is_left(ch):
                stack.append(ch)
            elif is_right(ch):
                # why first itself is right?
                if len(stack) == 0:
                    return False
                if are_pair(stack[len(stack) - 1], ch):
                    stack.pop(len(stack) - 1)
                else:
                    return False

        return len(stack) == 0