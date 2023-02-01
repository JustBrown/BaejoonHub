from collections import deque

def bfs(start):
    q = deque([start])
    cnt[start] = 0
    while q:
        cur_pos = q.popleft()
        for i in range(1, A[cur_pos]+1):
            next_pos = cur_pos+i
            if next_pos < n:
                if cnt[next_pos] > cnt[cur_pos]+1:
                    cnt[next_pos] = cnt[cur_pos]+1
                    q.append(next_pos)

n = int(input())
A = list(map(int, input().split()))

cnt = [float('inf') for _ in range(n)]
bfs(0)

print(-1 if cnt[n-1]==float('inf') else cnt[n-1])