import sys
input = sys.stdin.readline

n = int(input())
start_end = list(map(int, input().split()))
start, end = start_end[:2], start_end[2:]
dists = [0]*n

for i in range(n):
    cur, next = start[:], [0, 0]
    for j in range(int(input())):
        next = list(map(int, input().split()))
        dists[i] += abs(cur[0]-next[0])+abs(cur[1]-next[1])
        cur = next[:]
    dists[i] += abs(cur[0]-end[0])+abs(cur[1]-end[1])

print(dists.index(min(dists))+1)