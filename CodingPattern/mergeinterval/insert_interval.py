def insert(intervals, new_interval):
    merged = []
    i, start, end = 0, 0, 1

    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i +=1

    while i < len(intervals) and intervals[i][start] < new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i +=1
    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i +=1
    return merged

print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))

