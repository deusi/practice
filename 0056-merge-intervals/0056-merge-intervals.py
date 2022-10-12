class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if end >= s:
                end = max(end, e)
            else:
                result.append((start, end))
                start, end = s, e
        result.append((start, end))
        return result