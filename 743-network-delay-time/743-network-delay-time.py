from collections import deque
from heapq import heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        reach = {}
        for time in times:
            if time[0] in reach:
                heappush(reach[time[0]], [time[2], time[1]])
            else:
                reach[time[0]] = [[time[2], time[1]]]
                
        distanceReached = [inf for _ in range(n + 1)]
        distanceReached[0], distanceReached[k] = 0, 0
        
        queue = deque([k])
        while queue:
            node = queue.popleft()
            
            if node not in reach:
                continue
                
            for elem in reach[node]:
                time, nextVal = elem
                if distanceReached[node] + time < distanceReached[nextVal]:
                    distanceReached[nextVal] = distanceReached[node] + time
                    queue.append(nextVal)
                    
        delay = max(distanceReached)
        if delay == inf:
            return -1
        return delay