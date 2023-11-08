# generating the graph  
graph = { 
    'A': ['B', 'C', 'D'], 
    'B': ['A'], 
    'C': ['A', 'D'], 
    'D': ['A', 'C', 'E'], 
    'E': ['D'], 
} 
def bfs(node): 
    # keeping the track of the visited nodes 
    visited = set() 
    # To track the adjacent nodes of the previously visited nodes 
    queue = [] 
 
    visited.add(node) 
    queue.append(node) 
 
    while queue: 
        # getting the front elements of the queue 
        v = queue.pop(0) 
        print(v, end=" ") 
        # after getting the node from the queue check whether it's adjacent nodes are visited 
        for i in graph[v]: 
            # updating the list if the node not present in the list 
            if i not in visited: 
                visited.add(i) 
                queue.append(i) 
# Entering the starting vertex for the graph traversal 
bfs('A') 