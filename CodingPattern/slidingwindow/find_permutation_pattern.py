def find_permutation(str, pattern):
    char_freq ={}
    start, match = 0, 0
    for char in pattern:
        if char not in char_freq:
            char_freq[char] =0
        char_freq[char] += 1

    for end in range(len(str)):
        right_char = str[end]
        if right_char in char_freq:
            char_freq[right_char] -=1
            if char_freq[right_char] ==0:
                match +=1

        if match == len(char_freq):
            return True

        if end >= len(pattern) -1:
            left_char = str[start]
            start +=1
            if left_char in char_freq:
                if char_freq[left_char] ==0:
                    match -= 1
                char_freq[left_char] +=1

    return False

print('Permutation exist: ' + str(find_permutation("faadaabbc", "aabbc")))




