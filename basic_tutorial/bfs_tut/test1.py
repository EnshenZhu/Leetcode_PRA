# source https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        # print(s, end="")

        for neighbour in graph[s]:
            print(neighbour)


# Driver Code
bfs(visited, graph, 'A')
