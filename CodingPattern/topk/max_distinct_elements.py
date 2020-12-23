from heapq import *

def find_maximum_distinct_elements(nums, k):
    distinctelements=0
    min_heap = []
    if len(nums) < k:
        return nums
    frequency = {}
    for element in nums:
        frequency[element] = frequency.get(element,0)+1

    for key, v in frequency.items():
        if v ==1:
            distinctelements += 1
        else:
            heappush(min_heap, (v,key))

    while k>0 and min_heap:
        f, element = heappop(min_heap)
        k -=f-1
        if k >= 0:
            distinctelements +=1

    if k>0:
        distinctelements -= k

    return distinctelements


def main():

  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
