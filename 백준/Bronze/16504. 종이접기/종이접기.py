import sys
input = sys.stdin.readline

n = int(input())
result = 0
for _ in range(n):
    result += sum(list(map(int, input().split())))

print(result)