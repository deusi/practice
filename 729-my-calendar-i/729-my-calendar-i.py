class MyCalendar:

    def __init__(self):
        self.slots = collections.deque()

    def book(self, start: int, end: int) -> bool:
        if not self.slots or self.slots[-1][1] <= start:
            self.slots.append([start, end])
            return True
        elif end <= self.slots[0][0]:
            self.slots.appendleft([start, end])
            return True
        for i in range(1, len(self.slots)):
            if self.slots[i - 1][1] <= start and self.slots[i][0] >= end:
                self.slots.insert(i, [start, end])
                return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)