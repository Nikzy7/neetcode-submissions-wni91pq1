class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            queue = []
            queue.append((r, c))
            visited.add((r, c))

            area = 0

            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            while queue:
                curr_r, curr_c = queue.pop(0)

                for dr, dc in directions:
                    if curr_r + dr in range(rows) and curr_c + dc in range(cols):
                        if grid[curr_r + dr][curr_c + dc] == 0:
                            area += 1
                        if (curr_r + dr, curr_c + dc) not in visited and grid[
                            curr_r + dr
                        ][curr_c + dc] == 1:
                            visited.add((curr_r + dr, curr_c + dc))
                            queue.append((curr_r + dr, curr_c + dc))
                    else:
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)

        return 0
