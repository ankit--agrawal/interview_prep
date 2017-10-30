def dfs_iterative(graph,start):
    stack = [start], path = []
    while stack: #stack not empty
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for n in graph[vertex]:
            stack.append(n)

    return path

G = {1:[2,3], 2:[4,5], 3:[5], 4:[6],5:[6],6:[7],7:[]}
print dfs_iterative(G,1)
