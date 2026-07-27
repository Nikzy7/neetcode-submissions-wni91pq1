class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate_3x3(r, c) -> bool:
            def find_range(pos) -> tuple(int, int):
                if pos in range(0, 3):
                    return (0, 3)
                elif pos in range(3, 6):
                    return (3, 6)
                else:
                    return (6, 9)

            row_range_start, row_range_end = find_range(r)
            col_range_start, col_range_end = find_range(c)

            current_element = board[r][c]

            for row in range(row_range_start, row_range_end):
                for col in range(col_range_start, col_range_end):
                    if row != r and col != c:
                        if board[row][col] == current_element:
                            return False

            return True

        def validate_row(r, c) -> bool:
            current_element = board[r][c]

            for column in range(9):
                if column != c:
                    if board[r][column] == current_element:
                        return False

            return True

        def validate_column(r, c) -> bool:
            current_element = board[r][c]

            for row in range(9):
                if row != r:
                    if board[row][c] == current_element:
                        return False
            return True

        for row in range(9):
            for column in range(9):
                if board[row][column] != ".":
                    is_valid = (
                        validate_row(row, column)
                        and validate_column(row, column)
                        and validate_3x3(row, column)
                    )

                    if not is_valid:
                        return False

        return True
