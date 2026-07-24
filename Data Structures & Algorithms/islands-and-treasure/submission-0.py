class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        rows = len(grid)
        cols = len(grid[0])

        def bfs(queue):
            current_distance = 1
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            visited = set()

            while queue:
                nodes_to_pop = len(queue)

                for _ in range(nodes_to_pop):
                    curr_r, curr_c = queue.pop(0)

                    for dr, dc in directions:
                        if curr_r + dr in range(rows) and curr_c + dc in range(cols):
                            if (
                                grid[curr_r + dr][curr_c + dc] == INF
                                and (curr_r + dr, curr_c + dc) not in visited
                            ):
                                grid[curr_r + dr][curr_c + dc] = current_distance
                                visited.add((curr_r + dr, curr_c + dc))
                                queue.append((curr_r + dr, curr_c + dc))

                current_distance += 1

        treasures = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    treasures.append((r, c))

        bfs(treasures)
