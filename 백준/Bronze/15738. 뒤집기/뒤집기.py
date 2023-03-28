import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
array = list(map(int, input().split()))
for _ in range(m):
    i = int(input())
    start, end = (1, i) if i>0 else (n+i+1, n)
    
    if k<start or k>end:
        continue
    k = (i+1)-k if i>0 else (2*n+i+1)-k
print(k)