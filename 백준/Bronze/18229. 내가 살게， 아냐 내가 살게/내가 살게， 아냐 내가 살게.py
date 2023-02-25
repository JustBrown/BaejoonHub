import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dist = [0]*n
for i in range(m):
    for j in range(n):
        dist[j] += array[j][i]
        if dist[j] >= k:
            print(j+1, i+1)
            sys.exit()