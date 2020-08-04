def DFS(start):
    visited[start] = True
    print(start, end = ' ')
    for next in range(1, n + 1):
        if e[start][next] and visited[next] == False:
            DFS(next)

def BFS(start):
    q = [start]
    visited[start] = False
    while len(q) > 0:
        front = q[0]
        print(front, end = ' ')
        q.pop(0)
        for next in range(1, n + 1):
            if e[front][next] and visited[next]:
                visited[next] = False
                q.append(next)

n, m, start = map(int, input().split())
e = [[0 for x in range(n + 1)] for y in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    e[u][v] = 1
    e[v][u] = 1

DFS(start)
print(visited)
print()
BFS(start)
print(visited)