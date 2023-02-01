import sys
from collections import deque
input = sys.stdin.readline

def bfs(starts):
    q = deque(starts)
    date = 0
    moves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
             (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while q:
        i, j, k = q.popleft()
        date = dates[i][j][k]
        for dz, dy, dx in moves:
            z = i + dz
            y = j + dy
            x = k + dx
            if 0 <= z < H and 0 <= y < N and 0 <= x < M:
                if array[z][y][x] == 0:
                    q.append((z, y, x))
                    array[z][y][x] = 1
                    dates[z][y][x] = date + 1

# 초기화 (array[h][n][m]으로 접근)
M, N, H = map(int, input().split())
dates = [[[0]*M for n in range(N)] for h in range(H)]
array = [[] for h in range(H)]
for h in range(H):
    for n in range(N):
        array[h].append(list(map(int, input().split())))

# array 값이 1인 starts의 좌표 찾기
starts = list()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if array[h][n][m] == 1:
                starts.append((h, n, m))

# bfs 실행 및 결과도출
bfs(starts)
max_date = max(sum(sum(dates, []), []))
print(-1 if 0 in set(sum(sum(array, []), [])) else max_date)
