from itertools import combinations

def find_subsets(nums):
    subset = []
    subset.append([])
    for number in nums:
        n = len(subset)
        for i in range(n):
            set = list(subset[i])
            set.append(number)
            subset.append(set)

    return subset


def main():

  print("Here is the list of subsets: " + str(find_subsets([1,3,3])))
  #print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()