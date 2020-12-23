from heapq import *
def find_closest_elements(arr, K, X):
  result = []
  max_heap = []

  for element in arr:
      diff = abs(element-X)
      if len(max_heap) >= K:
          diff1, nbr = max_heap[0]
          if diff < -diff1:
              heappop(max_heap)
              heappush(max_heap, (-diff,element))
      else:
          heappush(max_heap, (-diff, element))

  for i in range(K):
      diff, element = heappop(max_heap)
      result.append(element)

  return result


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()