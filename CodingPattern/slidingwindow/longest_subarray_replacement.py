def length_of_longest_substring(arr, k):
    start, max_len, max_freq = 0,0,0
    freq ={}
    for end in range(len(arr)):
        if arr[end] not in freq:
            freq[arr[end]] =0
        freq[arr[end]] +=1

        while freq[0] > k:
            left = arr[start]
            freq[left] -=1
            start +=1

        max_len = max(max_len, end-start+1)

    return max_len

print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],2))
