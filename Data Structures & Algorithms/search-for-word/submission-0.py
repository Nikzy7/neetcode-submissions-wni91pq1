class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, char_ptr_to_match):
            if char_ptr_to_match == len(word):
                return True

            if r not in range(rows) or c not in range(cols):
                return False

            if word[char_ptr_to_match] != board[r][c]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, char_ptr_to_match + 1)
                or dfs(r - 1, c, char_ptr_to_match + 1)
                or dfs(r, c + 1, char_ptr_to_match + 1)
                or dfs(r, c - 1, char_ptr_to_match + 1)
            )

            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    found = dfs(r, c, 0)

                    if found:
                        return True

        return False
