class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        rows = len(board)
        cols = len(board[0])

        self.can_mark = set()

        def bfs(r, c):
            queue = []
            queue.append((r, c))
            visited.add((r, c))

            current_can_mark = set()

            valid = True  # if any element of the island is touch extra

            while queue:
                curr_r, curr_c = queue.pop(0)

                directions_seen = 0

                for dr, dc in directions:
                    if curr_r + dr in range(rows) and curr_c + dc in range(cols):
                        directions_seen += 1
                        if (
                            board[curr_r + dr][curr_c + dc] == "O"
                            and (curr_r + dr, curr_c + dc) not in visited
                        ):
                            visited.add((curr_r + dr, curr_c + dc))
                            queue.append((curr_r + dr, curr_c + dc))

                if directions_seen == 4:
                    current_can_mark.add((curr_r, curr_c))
                else:
                    valid = False

            if valid:
                # print(f"doing union {self.can_mark} and {current_can_mark}")
                self.can_mark = self.can_mark.union(current_can_mark)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and board[r][c] == "O":
                    bfs(r, c)

        ## mark the board from can_mark

        for r, c in self.can_mark:
            board[r][c] = "X"
