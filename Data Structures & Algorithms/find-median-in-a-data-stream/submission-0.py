class Heap:
    def __init__(self,is_max_heap=False):
        self.heap = []
        self.is_max_heap = is_max_heap

        heapq.heapify(self.heap)

    def __str__(self):
        return str([x*-1 for x in self.heap] if self.is_max_heap else [x for x in self.heap])

    def length(self):
        return len(self.heap)

    def push(self, num):
        if self.is_max_heap:
            heapq.heappush(self.heap, -1 * num)
        else:
            heapq.heappush(self.heap,num)

    def pop(self):
        to_return = heapq.heappop(self.heap)
        if self.is_max_heap:
            return -1 * to_return
        return to_return

    def peek(self):
        return self.heap[0] * -1 if self.is_max_heap else self.heap[0]

class MedianFinder:

    def __init__(self):
        self.maxHeap = Heap(is_max_heap=True) # left side
        self.minHeap = Heap() # right side

    def addNum(self, num: int) -> None:
        if self.maxHeap.length() == 0 and self.minHeap.length() == 0:
            self.maxHeap.push(num)
        elif self.maxHeap.length() == 0:
            if self.minHeap.peek() < num:
                temp = self.minHeap.pop()
                self.maxHeap.push(temp)
            self.minHeap.push(num)
            
        else:  
            if self.maxHeap.length() == self.minHeap.length():
                if num < self.maxHeap.peek():
                    self.maxHeap.push(num)
                else:
                    self.minHeap.push(num)
            elif self.maxHeap.length() > self.minHeap.length():
                if self.maxHeap.peek() > num:
                    temp = self.maxHeap.pop()
                    self.minHeap.push(temp)
                    self.maxHeap.push(num)
                else:
                    self.minHeap.push(num)
            elif self.maxHeap.length() < self.minHeap.length():
                if self.minHeap.peek() < num:
                    temp = self.minHeap.pop()
                    self.maxHeap.push(temp)
                    self.minHeap.push(num)
                else:
                    self.maxHeap.push(num)

        print(f"maxHeap left :: {self.maxHeap}")
        print(f"minHeap right :: {self.minHeap}\n\n")

    def findMedian(self) -> float:
        # print(self.minHeap.length())
        # print(self.maxHeap.length())
        # print((self.minHeap.length() + self.maxHeap.length() % 2))
        if ((self.minHeap.length() + self.maxHeap.length()) % 2) == 0:
            print(self.minHeap.peek())
            print(self.maxHeap.peek())
            return (self.minHeap.peek() + self.maxHeap.peek()) / 2

        # minHeap bigger
        if self.minHeap.length() > self.maxHeap.length():
            print("if")
            return self.minHeap.peek()

        print("else")
        return self.maxHeap.peek()