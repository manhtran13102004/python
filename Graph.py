class Graph:
    
    def __init__(self, edges):
        self.dict = {}
        for start, end in edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start] = [end]
            
    def get_paths(self, start, end, visited=[]):
        visited = visited + [start]
        if start == end:
            return [visited]
        elif start not in self.dict:
            return []
        
        paths = []
        for child in self.dict[start]:
            if child not in visited:
                child_paths = self.get_paths(child, end, visited)
                for child_path in child_paths:
                    paths.append(child_path)
        
        return paths
    
    def get_shortest_path(self, start, end, visited=[]):
        visited = visited + [start]
        if start == end:
            return visited
        elif start not in self.dict:
            return []
        
        shortest_path = None
        for child in self.dict[start]:
            if child not in visited:
                child_path = self.get_shortest_path(child, end, visited)
                if child_path and (shortest_path == None or len(child_path) < len(shortest_path)):
                    shortest_path = child_path
                    
        return shortest_path
    
    def get_shortest_path2(self, start, end):
        if start not in self.dict:
            return None
        from collections import deque
        visited = set()        
        visited.add(start)
        queue = deque()
        queue.appendleft([start])
        
        while len(queue) > 0:
            candidate_path = queue.pop()
            if candidate_path[-1] == end:
                return candidate_path
            
            if candidate_path[-1] not in self.dict:
                continue
            
            for child in self.dict[candidate_path[-1]]:
                if child not in visited:
                    visited.add(child)
                    queue.appendleft(candidate_path + [child])
        return None
        
    
routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

route_graph = Graph(routes)

start = "Paris"
end = "New York"

print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path2(start,end))
