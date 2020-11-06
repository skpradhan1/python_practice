class Interval:
      def __init__(self, start, end):
          self.start = start
          self.end = end

      def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  merged = []
  if len(intervals) < 2:
      return intervals

  intervals.sort(key= lambda x: x.start)
  start = intervals[0].start
  end = intervals[0].end
  for i in range(1,len(intervals)):
      interval = intervals[i]
      if interval.start < end:
          end = max(end, interval.end)
      else:
          merged.append(Interval(start, end))
          start = interval.start
          end = interval.end
  merged.append(Interval(start, end))
  return merged


def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

main()