def find_duplicate(nums):
    i,n = 0, len(nums)
    while i < n:
        j = nums[i] -1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i +=1
    for i in range(n):
        if nums[i] != i+1:
            return nums[i]


print(find_duplicate([2, 1, 3, 3, 5, 4]))