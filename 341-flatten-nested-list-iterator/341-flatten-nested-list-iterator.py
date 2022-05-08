# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._generator = self._int_generator(nestedList)
        self._peek = None
        
    def _int_generator(self, nList):
        for num in nList:
            if num.isInteger():
                yield num.getInteger()
            else:
                yield from self._int_generator(num.getList())
    
    def next(self) -> int:
        if not self.hasNext():
            return None
        nextElem, self._peek = self._peek, None
        return nextElem
    
    def hasNext(self) -> bool:
        if self._peek != None:
            return True
        try:
            num = next(self._generator)
            self._peek = num
            return True
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())