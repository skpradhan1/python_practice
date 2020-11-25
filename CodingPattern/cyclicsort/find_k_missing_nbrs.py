def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    for i in range(n):
        if len(missingNumbers) < k:
            if nums[i] != i+1:
                missingNumbers.append(i+1)

    last_ele = max(nums)

    while len(missingNumbers) < k:
        missingNumbers.append(last_ele+1)
        last_ele +=1
    return missingNumbers

print(find_first_k_missing_positive([-2, -3, 4], 2))


