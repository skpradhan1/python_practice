def search_next_letter(letters, key):
    start, end = 0, len(letters) -1
    if key > letters[end] or key < letters[0]:
        return letters[0]
    while start <= end:
        mid = start + (end-start)//2
        if letters[mid] is key:
            return letters[(mid+1) % len(letters)]
        elif letters[mid] > key:
            end = mid-1
        else:
            start = mid+1
    return letters[start % len(letters)]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))

main()