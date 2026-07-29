class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        if len(nums) >= k:
            self.heap = nums[:k]
        else:
            self.heap = nums

        heapq.heapify(self.heap)

        for iter in range(k, len(nums)):
            if nums[iter] > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, nums[iter])

    def add(self, val: int) -> int:
        if len(self.heap) != self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
