import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [-1] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev

def reconstruct_path(prev, target):
    path = []
    while target != -1:
        path.append(target)
        target = prev[target]
    return path[::-1]

# Nhập dữ liệu
n = int(input("Số đỉnh: "))
m = int(input("Số cạnh: "))
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input("Nhập cạnh (u v w): ").split())
    graph[u].append((v, w))

start = int(input("Nhập đỉnh bắt đầu: "))
dist, prev = dijkstra(graph, start)

for i in range(n):
    if dist[i] == float('inf'):
        print(f"Không có đường đến {i}")
    else:
        path = reconstruct_path(prev, i)
        print(f"Đường đi đến {i}: {' -> '.join(map(str, path))}, Chi phí: {dist[i]}")
