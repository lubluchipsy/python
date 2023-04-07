def dist(u):
    distance = []  
    stack = []
    distance = [-1 for _ in range(n_vertices)]
    distance[u] = 0

    for v in adj_list[u]:
        if distance[v] == -1:
            stack.append(v)
            distance[v] = distance[u] + 1
    while stack:
        u = stack.pop()
        for v in adj_list[u]:
            if distance[v] == -1:
                stack.append(v)
                distance[v] = distance[u] + 1
    return distance


n_vertices, n_edges = map(int, input().split())
vertices = set()
edges_list = []  #список ребер

for i in range(n_edges):
    u, v = map(int, input().split())
    edges_list.append([u, v])
    vertices.add(u)
    vertices.add(v)

adj_list = [set() for _ in range(n_vertices)]  #список смежности

for edge in edges_list:
    adj_list[edge[0]].add(edge[1])
    adj_list[edge[1]].add(edge[0])

distance = dist(0)
for i in range(n_vertices):
    print(distance[i])
