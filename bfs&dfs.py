from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    print("BFS traversal:", end=" ")
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()  

def dfs_recursive(graph, vertex, visited):
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    print("DFS traversal (iterative):", end=" ")
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            
            for neighbor in reversed(graph[vertex]):  # Reverse to maintain the order
                if neighbor not in visited:
                    stack.append(neighbor)
    print()  # For new line

def main():
    graph = {}
    print("Enter the graph edges (format: node neighbor). Type 'done' when finished:")

    while True:
        edge = input("Enter an edge (or type 'done'): ")
        if edge.lower() == 'done':
            break
        node, neighbor = edge.split()
        if node not in graph:
            graph[node] = []
        if neighbor not in graph:
            graph[neighbor] = []
        graph[node].append(neighbor)
        graph[neighbor].append(node)  # For undirected graph
    
    start_node = input("Enter the starting node for BFS and DFS: ")
    
    print("\nBFS traversal:")
    bfs(graph, start_node)
    
    print("\nDFS traversal (recursive):")
    visited = set()
    dfs_recursive(graph, start_node, visited)
    
    print("\nDFS traversal (iterative):")
    dfs_iterative(graph, start_node)

if __name__ == "__main__":
    main()
