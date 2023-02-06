import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(k*n):
    for j in range(k*n):
        print(array[i//k][j//k], end=' ')
    print()