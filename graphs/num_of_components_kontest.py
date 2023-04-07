def dfs(u):
    colors[u] = 1
    free_vertices.remove(u)
    for v in adj_list[u]:  #для соседей
        if colors[v] == 0:
            dfs(v)
    colors[u] = 2
    return

n_vertices = int(input())
n_edges = int(input())
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

colors = [0]*n_vertices

n_components = 0
free_vertices = set(range(n_vertices))
while free_vertices:
    for u in free_vertices:
        break
    dfs(u)
    n_components += 1
print(n_components)
