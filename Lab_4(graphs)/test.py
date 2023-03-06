graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
print(graph[0])
visited = [] # List to keep track of visited nodes.
queue = []   # Initialize a queue
def bfs(visited, graph, node, end, path):
    global queue
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end = " ")
        
        if s == end:
            # path[s] += 1
            return path
       
        for neighbour in graph[s]:
            if neighbour not in visited:
                path[neighbour] = path[s] + 1
                visited.append(neighbour)
                queue.append(neighbour)
    return []
# Driver Code
print(bfs(visited, graph, 'A', 'E', {'A':0}))