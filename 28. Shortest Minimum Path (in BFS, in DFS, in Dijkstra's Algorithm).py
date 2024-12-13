import heapq

# Define a simple graph representation as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Implement BFS (Breadth-First Search)
def bfs(graph, start, end):
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)

# Implement DFS (Depth-First Search)
def dfs(graph, start, end):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for neighbor in set(graph[node]) - set(path):
            if neighbor == end:
                return path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))

# Implement Dijkstra's algorithm
def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            path = path + [node]
            if node == end:
                return path
            visited.add(node)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))

# Test the search techniques
source = 'A'
destination = 'D'

bfs_path = bfs(graph, source, destination)
dfs_path = dfs(graph, source, destination)
dijkstra_path = dijkstra(graph, source, destination)

# Print the results in the console
print("Comparative Analysis on the Performance of Various Search Techniques")
print("Source:", source)
print("Destination:", destination)

print("\nBreadth-First Search:")
if bfs_path:
    print("Path:", ' -> '.join(bfs_path))
    print("Cost:", sum(graph[bfs_path[i]][bfs_path[i + 1]] for i in range(len(bfs_path) - 1)))
else:
    print("No path found")

print("\nDepth-First Search:")
if dfs_path:
    print("Path:", ' -> '.join(dfs_path))
    print("Cost:", sum(graph[dfs_path[i]][dfs_path[i + 1]] for i in range(len(dfs_path) - 1)))
else:
    print("No path found")

print("\nDijkstra's Algorithm:")
if dijkstra_path:
    print("Path:", ' -> '.join(dijkstra_path))
    print("Cost:", sum(graph[dijkstra_path[i]][dijkstra_path[i + 1]] for i in range(len(dijkstra_path) - 1)))
else:
    print("No path found")
