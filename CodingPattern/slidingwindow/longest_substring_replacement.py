def length_of_longest_substring(str, k):
    start, max_len, max_freq = 0,0,0
    char_f = {}
    for end in range(len(str)):
        if str[end] not in char_f:
            char_f[str[end]] = 0
        char_f[str[end]] +=1
        max_freq = max(max_freq, char_f[str[end]])

        while end-start+1-max_freq > k:
            left = str[start]
            char_f[left] -=1
            start +=1

        max_len = max(max_len, end-start+1)
    return max_len


print(length_of_longest_substring("aabccbb",2))