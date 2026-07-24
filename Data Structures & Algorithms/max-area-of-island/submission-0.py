class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        self.max_area = 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            queue = []
            queue.append((r, c))
            visited.add((r, c))

            current_area = 0

            while queue:
                curr_r, curr_c = queue.pop(0)
                current_area += 1

                for dr, dc in directions:
                    if curr_r + dr in range(rows) and curr_c + dc in range(cols):
                        if (
                            grid[curr_r + dr][curr_c + dc] == 1
                            and (curr_r + dr, curr_c + dc) not in visited
                        ):
                            queue.append((curr_r + dr, curr_c + dc))
                            visited.add((curr_r + dr, curr_c + dc))

            self.max_area = max(current_area, self.max_area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    bfs(r, c)

        return self.max_area