class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        components = 0


        def bfs(node):
            queue = []
            queue.append(node)
            visited.add(node)

            while queue:
                curr_node = queue.pop(0)

                for next_node in graph.get(curr_node,[]):
                    if next_node not in visited:
                        queue.append(next_node)
                        visited.add(next_node)


        for node in range(n):
            if node not in visited:
                bfs(node)
                components += 1

        return components