import sys
input = sys.stdin.readline

date = [0]*32
for _ in range(int(input())):
    s, e = map(int, input().split())
    for d in range(s, e):
        date[d] += 1

print(1 if max(date)<=int(input()) else 0)