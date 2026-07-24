class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            queue = []
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                curr_r, curr_c = queue.pop(0)

                for dr, dc in directions:
                    if curr_r + dr in range(rows) and curr_c + dc in range(cols):
                        if (
                            grid[curr_r + dr][curr_c + dc] == "1"
                            and (curr_r + dr, curr_c + dc) not in visited
                        ):
                            queue.append((curr_r + dr, curr_c + dc))
                            visited.add((curr_r + dr, curr_c + dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands
