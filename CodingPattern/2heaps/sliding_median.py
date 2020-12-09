from heapq import *
import heapq

class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for i in range(len(nums)-k+1)]
        for i in range(len(nums)-k+1):
            if not self.maxHeap or -self.maxHeap[0] > nums[i]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            self.rebalance()

            if i-k+1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    result[i-k+1] = -self.maxHeap[0]/2.0 + self.minHeap[0]/2.0
                else:
                    result[i-k+1] = -self.maxHeap[0]
                element = nums[i-k+1]
                if element <= -self.maxHeap[0]:
                    self.remove(-element, self.maxHeap)
                else:
                    self.remove(element, self.minHeap)
                self.rebalance()
        return result

    def remove(self, element, heap):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]
        heapify(heap)


    def rebalance(self):
        if len(self.maxHeap) > len(self.minHeap) +1 :
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()