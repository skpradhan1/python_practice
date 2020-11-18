from heapq import *
class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

def min_meeting_rooms(meetings:list):
    meetings.sort(key=lambda x : x.start)
    minRooms = 0
    minHip = []
    for meeting in meetings:
        while len(minHip) > 0 and meeting.start >= minHip[0].end:
            heappop(minHip)
        heappush(minHip,meeting)
        minRooms = max(len(minHip), minRooms)
    return minRooms

def main():
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))

main()

