def find_first_missing_positive(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  print(nums)

  for i in range(n):
    if nums[i] != i + 1:
      return i + 1


print(find_first_missing_positive([1,2,3,4,4]))


