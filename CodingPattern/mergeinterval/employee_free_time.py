from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class EmpInterval:
    def __init__(self, interval, empIndex, intervalIndex):
        self.interval = interval
        self.empIndex = empIndex
        self.intervalIndex = intervalIndex

    def __lt__(self, other):
        return self.interval.start < other.interval.start

def find_employee_free_time(schedule):
    if schedule is None:
        return []
    n = len(schedule)
    result, minHeap = [], []
    for i in range(n):
        heappush(minHeap, EmpInterval(schedule[i][0],i,0))

    prev = minHeap[0].inteval
    while minHeap:
        queueTop = heappop(minHeap)
        if prev.end < queueTop.interval.start:
            result.append(Interval(prev.end,queueTop.interval.start))
            prev = queueTop.interval
        else:
            if prev.end < queueTop.interval.end:
                prev = queueTop.interval
        empSchedule =schedule[queueTop.empIndex]
        if len(empSchedule) > queueTop.intervalIndex+1:
            heappush(minHeap, EmpInterval(empSchedule[queueTop.intervalIndex+1],
                                          queueTop.empIndex,queueTop.intervalIndex+1))
    return result






