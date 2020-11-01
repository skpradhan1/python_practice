def find_substring(str, pattern):
    start, matched = 0, 0
    freq = {}
    min_len = float('inf')
    for char in pattern:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    for end in range(len(str)):
        right_char = str[end]
        if right_char in freq:
            freq[right_char] -= 1
            if freq[right_char] == 0:
                matched +=1
        if matched == len(freq):
            min_len = min(min_len, end - start + 1)
            start +=1
            left_char = str[start]
            if left_char in freq:
                freq[left_char] +=1
                if freq[left_char] ==0:
                    matched -= 1
    return min_len

print(find_substring('aabdec','abc'))




