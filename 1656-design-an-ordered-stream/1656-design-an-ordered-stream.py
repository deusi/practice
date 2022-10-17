class OrderedStream:

    def __init__(self, n: int):
        self.values = [None] * (n + 2)
        self.ptr = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey] = value
        while self.values[self.ptr]:
            self.ptr += 1
        else:
            return self.values[idKey:self.ptr]
        return []

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)