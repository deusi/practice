# since python queue is deque in disguise, we use deque and limit the operations we are allowed to use
from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.topElem = None
    
    # push in O(1)
    def push(self, x: int) -> None:
        self.q1.append(x)
        self.topElem = x
    
    # pop in O(n)
    def pop(self) -> int:
        # push all but 2 elements from queue1 to queue2
        while len(self.q1) > 2:
            e = self.q1.popleft()
            self.q2.append(e)
        # push second elements to queue2 and make this element on top
        if len(self.q1) > 1:
            e = self.q1.popleft()
            self.q2.append(e)
            self.topElem = e
        # pop the last element
        e = self.q1.popleft()
        
        self.q2, self.q1 = self.q1, self.q2
        return e

    def top(self) -> int:
        return self.topElem

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()