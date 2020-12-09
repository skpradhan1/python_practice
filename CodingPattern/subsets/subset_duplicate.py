def find_subsets(nums):
    subsets = []
    nums.sort()
    subsets.append([])
    prev = None
    new_list = []
    for element in nums:
        if element is prev:
            n = len(new_list)
            for i in range(n):
                sets = list(new_list[i])
                sets.append(element)
                subsets.append(sets)
        else:
            n = len(subsets)
            new_list = []
            for i in range(n):
                sets = list(subsets[i])
                sets.append(element)
                subsets.append(sets)
                new_list.append(sets)
            prev = element
    return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
