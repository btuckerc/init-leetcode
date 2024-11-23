def kruskal(edges, num_nodes):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    parent = list(range(num_nodes))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX != rootY:
            parent[rootX] = rootY

    mst = []
    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
    return mst
