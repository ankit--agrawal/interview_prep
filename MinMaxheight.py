from math import log, floor
def minHeight(graph):
    n = len(graph.keys())
    if n == 0 or n == 1: return 0
    else: return floor(log(n,2))

def maxHeight(graph):
    n = len(graph.keys())
    if n == 0 or n == 1: return 0
    else: return n-1

G = {1:[2,3], 2:[4,5], 3:[5], 4:[6],5:[6],6:[7],7:[]}
H = {1:[2,3],3:[6,7],4:[8],8:[12],5:[9],6:[10],7:[11],10:[13],9:[],11:[],12:[],13:[],2:[4,5]}
print minHeight(G), minHeight(H)
print maxHeight(G), maxHeight(H)
