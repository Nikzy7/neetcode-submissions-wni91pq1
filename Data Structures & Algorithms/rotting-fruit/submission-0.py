class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)  # m
        cols = len(grid[0])  # n

        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(queue):
            minutes_elapsed = 0

            while queue:
                # print(f"queue is {queue}")
                total_to_rot = len(queue)
                minutes_elapsed += 1

                for _ in range(total_to_rot):
                    # current row , current column
                    cr, cc = queue.pop(0)

                    # delta row , delta column
                    for dr, dc in directions:
                        if cr + dr in range(rows) and cc + dc in range(cols):
                            if (
                                grid[cr + dr][cc + dc] == 1
                                and (cr + dr, cc + dc) not in visited
                            ):
                                grid[cr + dr][cc + dc] = 2
                                visited.add((cr + dr, cc + dc))
                                queue.append((cr + dr, cc + dc))

            return minutes_elapsed - 1  # removing 1 because of initial rot

        time_consumed = 0

        initial_queue_for_multi_source_bfs = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r, c):
                    initial_queue_for_multi_source_bfs.append((r, c))

        time_consumed = bfs(initial_queue_for_multi_source_bfs)

        # print(grid)
        # print(visited)

        # checking any fresh oranges
        for r in range(rows):
            if 1 in grid[r]:
                return -1

        return time_consumed if time_consumed > 0 else 0