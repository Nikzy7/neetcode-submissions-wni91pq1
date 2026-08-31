class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        movements = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def traverse(row, col, current_set):
            visited = current_set
            visited.add((row, col))

            queue = deque()

            queue.append((row, col))

            while queue:
                total_to_pop = len(queue)

                for _ in range(total_to_pop):
                    curr_r, curr_c = queue.popleft()

                    for dr, dc in movements:
                        if curr_r + dr in range(ROWS) and curr_c + dc in range(COLS):
                            if heights[curr_r + dr][curr_c + dc] >= heights[curr_r][curr_c]:
                                if ((curr_r + dr), (curr_c + dc)) not in visited:
                                    queue.append(((curr_r + dr), (curr_c + dc)))
                                    visited.add(((curr_r + dr), (curr_c + dc)))

            return visited

        def traverse_pacific():
            pacific_set = set()

            # move top left
            for c in range(COLS):
                pacific_set = traverse(0, c, pacific_set)

            # move left column
            for r in range(ROWS):
                pacific_set = traverse(r, 0, pacific_set)

            return pacific_set

        def traverse_atlantic():
            atlantic_set = set()

            # move right column
            for r in range(ROWS):
                atlantic_set = traverse(r, COLS - 1, atlantic_set)

            # move bottom row
            for c in range(COLS):
                atlantic_set = traverse(ROWS - 1, c, atlantic_set)

            return atlantic_set

        commons = list(traverse_pacific().intersection(traverse_atlantic()))

        answer = []

        for r, c in commons:
            answer.append([r, c])

        return answer
