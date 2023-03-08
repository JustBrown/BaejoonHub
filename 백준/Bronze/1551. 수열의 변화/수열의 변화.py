n, k = map(int, input().split())
A = list(map(int, input().split(',')))

for _ in range(k):
    B = [0]*(len(A)-1)
    for i in range(1, len(A)):
        B[i-1] = A[i]-A[i-1]
    A = B[:]

print(','.join(map(str, A)))