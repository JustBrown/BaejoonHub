import sys
input = sys.stdin.readline

date = [0]*32
for _ in range(int(input())):
    s, e = map(int, input().split())
    for d in range(s, e):
        date[d] += 1
k = int(input())

print(1 if max(date)<=k else 0)