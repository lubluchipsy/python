def dfs(u):
    visited = []  # если вершина v посещена, visited[v] == True
    stack = []
    visited = [False for _ in range(n_vertices)]
    visited[u] = True

    for v in adj_list[u]:
        if not visited[v]:
            stack.append(v)

    while stack:
        u = stack.pop()
        visited[u] = True
        for v in adj_list[u]:
            if not visited[v]:
                stack.append(v)
    return visited

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

    print(adj_list)
    print(dfs(0))

