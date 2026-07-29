class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # storing this way in minHeap (distance,(points))

        heap = []
        heapq.heapify(heap)

        def distance_from_origin(x,y):
            return math.sqrt(abs(x**2)+abs(y**2))

        for point in points:
            distance = distance_from_origin(point[0],point[1])

            if len(heap) < k:
                heapq.heappush(heap,(-1 * distance,point))
            else:
                if distance <= -1 * heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-1*distance,point))

        closest_points = []

        while heap:
            distance, point = heapq.heappop(heap)
            closest_points.append(point)

        return closest_points