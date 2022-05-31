from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph, inDegree = defaultdict(list), {}
        
        for i in range(1, n + 1):
            inDegree[i] = 0
            
        for parent, child in relations:
            graph[parent].append(child)
            inDegree[child] += 1
            
        queue = deque()
        for node in inDegree:
            if inDegree[node] == 0:
                queue.append(node)
                
        semesters = 0
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in graph[node]:
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        del inDegree[child]
                        queue.append(child)
                        
        return semesters if sum(inDegree.values()) == 0 else -1