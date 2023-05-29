N, K = map(int, input().split())

if N < sum(range(1, K+1)):
    print(-1)
else:
    point = sum(range(1, K+1)) % K
    print(K-1 if N % K == point else K)