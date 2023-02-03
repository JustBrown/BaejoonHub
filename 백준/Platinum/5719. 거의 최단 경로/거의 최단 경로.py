import heapq
from collections import deque
import sys
input = sys.stdin.readline

def dijkstra(start):
    dists[start] = 0
    heap = [(dists[start], start)]

    while heap:
        dist, node = heapq.heappop(heap)
        for e, d in graph[node]:
            if dists[node] < dist:
                continue
            next_dist = dist+d
            if dropped[node][e]:
                continue
            if dists[e] > next_dist:
                dists[e] = next_dist
                heapq.heappush(heap, (dists[e], e))

def bfs(end):
    q = deque([end])
    while q:
        node = q.popleft()
        if node == start:
            continue
        for post_e, post_dist in b_graph[node]:
            if dropped[post_e][node]:
                continue
            if dists[node]-dists[post_e] == post_dist:
                dropped[post_e][node] = True
                q.append(post_e)

while True:
    n, m = map(int, input().split())
    if n==0 and m==0:
        break
    start, end = map(int, input().split())
    graph = [[] for _ in range(n)]
    b_graph = [[] for _ in range(n)]
    trace_list = set()
    dropped = [[False]*n for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v,p))
        b_graph[v].append((u,p))

    # 최단 겨올 구하기: dijkstra 실행
    dists = [float('inf')]*n
    dijkstra(start)

    # graph에서 최단 거리에 포함된 경로 지우기
    bfs(end)

    # 거의 최단경로 구하기: dijkstra 다시실행
    dists = [float('inf')]*n
    dijkstra(start)

    # 결과 출력
    print(dists[end] if dists[end]!=float('inf') else -1)
