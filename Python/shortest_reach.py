
# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach

t = int(input().strip())

def calculate_cost(nodes, travel_edges):    
    new_edges = []
    weight = 6
    current_cost = 0

    while travel_edges:
        for e in travel_edges:
            id, cost, edges = nodes[e-1]
            
            if cost == -1:
                new_edges = new_edges + edges
                cost = current_cost
                nodes[e-1] = (id, cost, edges)
            
        travel_edges = new_edges
        new_edges = []
        current_cost += weight
                
    return nodes
    
for test in range(t):
    n, m = [int(i) for i in input().strip().split()]
    
    nodes = [(i, -1, []) for i in range(1, n+1)]

    for edge in range(m):
        start, end = [int(i) for i in input().strip().split()]
        
        id, cost, edges = nodes[start-1]
        nodes[start-1] = (id, cost, edges + [end])

        id, cost, edges = nodes[end-1]
        nodes[end-1] = (id, cost, edges + [start])
        
    s = int(input().strip())
    
    nodes = calculate_cost(nodes, [s])
    
    weights = ' '.join([str(node[1]) for node in nodes if node[1] != 0])
    
    print(weights)