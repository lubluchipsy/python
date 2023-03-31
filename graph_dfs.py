def dfs(u):
    colors[u] = 1
    for v in adj_list[u]:  #для соседей
        if colors[v] == 0:
            dfs(v)
    colors[u] = 2
    return

if __name__ == "__main__":
    n_edges = int(input())
    vertices = set()
    edges_list = []  #список ребер

    for i in range(n_edges):
        u, v = map(int, input().split())
        edges_list.append([u, v])
        vertices.add(u)
        vertices.add(v)

    n_vertices = max(vertices) + 1
    adj_list = [set() for _ in range(n_vertices)]  #список смежности

    for edge in edges_list:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])

    colors = [0]*n_vertices
    print(adj_list)
    dfs(0)
    print(colors)


