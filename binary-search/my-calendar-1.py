class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int):
        left, right = 0, len(self.calendar) - 1
        # assign the last new index so that it can be added at the end if not valid position found in the middle
        result = len(self.calendar)

        while left <= right:
            mid = left + (right - left) // 2
            # check which half the new set of time will be placed

            # if there is a start time already bigger than the new start time, then move the right pointer as it
            # currently points to the end
            if self.calendar[mid][0] > start:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        # checking for overlapping condition

        # if half is for start time and the other half is for end time
        if (result > 0 and self.calendar[result - 1][1] > start) or (
                result < len(self.calendar) and self.calendar[result][0] < end):
            return False

        self.calendar.insert(result, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
times = [(10, 20), (15, 25), (20, 30)]
for s, e in times:
    param_1 = obj.book(s, e)
    print(param_1)
