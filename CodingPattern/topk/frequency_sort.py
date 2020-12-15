from heapq import *

def sort_character_by_frequency(str):
    str_new = ""
    char_map = {}
    for char in str:
        char_map[char] = char_map.get(char,0) +1

    max_heap = []
    for k, val in char_map.items():
        heappush(max_heap,(-val,k))

    while max_heap:
        k, v = heappop(max_heap)
        for i in range(-1*k):
            str_new += v

    return str_new



def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()