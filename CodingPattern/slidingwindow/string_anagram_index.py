from collections import Counter


def find_string_anagrams(str, pattern):
    result_index = []
    k = len(pattern)
    for i in range(len(str)-k+1):
        str1 = str[i:i+k]
        if Counter(str1) == Counter(pattern):
            result_index.append(i)
    return result_index

print(find_string_anagrams('abbcabc','abc'))
print(find_string_anagrams('ppqp','pq'))
