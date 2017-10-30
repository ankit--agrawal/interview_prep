def bfs_iterative(graph,start):
    queue = [start], path = []
    while queue:
        vertex = queue.pop()
        if vertex not in path:
            path.append(vertex)
            queue.append(graph[vertex] - path)
        return path

G = {1:[2,3], 2:[4,5], 3:[5], 4:[6],5:[6],6:[7],7:[]}
print bfs_iterative(G,1)
