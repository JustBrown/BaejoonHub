import sys
from math import ceil
input = sys.stdin.readline

students = [[0, 0] for _ in range(6)]
n, k = map(int, input().split())
for _ in range(n):
    s, y = map(int, input().split())
    students[y-1][s] += 1

result = 0
for s in sum(students, []):
    result += ceil(s/k)
print(result)