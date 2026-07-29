class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for source,destination,cost in times:
            graph[source].append((destination,cost))

        # (weight, node)
        minHeap = []
        heapq.heapify(minHeap)

        heapq.heappush(minHeap,(0,k)) # k is the starting node

        visited = set()

        time_consumed = 0

        while minHeap:
            current_weight, current_edge = heapq.heappop(minHeap)

            if current_edge in visited:
                continue

            visited.add(current_edge)

            time_consumed = max(time_consumed, current_weight)

            for next_edge, next_weight in graph.get(current_edge,[]):
                if next_edge not in visited:
                    heapq.heappush(minHeap,(current_weight+next_weight,next_edge))

        return time_consumed if len(visited) == n else -1