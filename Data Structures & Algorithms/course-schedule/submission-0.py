class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites is None:
            return True

        graph = defaultdict(list)

        for node, edge in prerequisites:
            graph[node].append(edge)

        visited = set()

        def dfs(node):
            if node in visited:
                return False

            if len(graph.get(node, [])) == 0:
                return True

            visited.add(node)
            for next_course in graph.get(node, []):
                if not dfs(next_course):
                    return False
            visited.remove(node)

            graph[node] = []
            return True

        for node in graph.keys():
            if not dfs(node):
                return False

        return True
