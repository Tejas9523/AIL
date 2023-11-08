def dfs(node, graph, visited, component): 
# Store the node in the list 
    output.append(node)   
    # Mark visited node 
    visited[node] = True   
    # Traverse to each adjacent node of a node 
    for child in graph[node]: 
        # Check whether the node is visited or not 
        if not visited[child]:   
            dfs(child, graph, visited, output)   
# Graph of nodes 
graph = { 
0: [2], 
1: [2, 3], 
2: [0, 1, 4], 
3: [1, 4], 
4: [2, 3] 
} 
# Starting node 
node = 0   
# Make all nodes to False initially 
visited = [False]*len(graph)   
# to store the sequence of the nodes 
output = [] 
dfs(node, graph, visited, output)   
print(f"Following is the Depth-first search: {output}")