from collections import deque
def bfs_iterative(graph,start):
    queue = deque(); path = []; queue.append(start);
    while queue:
        vertex = queue.popleft()
        if vertex not in path:
            path.append(vertex)
            for n in graph[vertex]: queue.append(n);
    return path

G = {1:[2,3], 2:[4,5], 3:[5], 4:[6],5:[6],6:[7],7:[]}
H = {1:[2,3],3:[6,7],4:[8],8:[12],5:[9],6:[10],7:[11],10:[13],9:[],11:[],12:[],13:[],2:[4,5]}
print bfs_iterative(G,1)
print bfs_iterative(H,1)
