import sys
input = sys.stdin.readline

n, q = map(int, input().split())
min_cost, num = float('inf'), 0
for i in range(1, n+1):
    p, k, c = map(int, input().split())
    cost = p
    t = (q//k-1 if q%k==0 else q//k)
    cost += t*(t+1)*c//2
    if min_cost > cost:
        min_cost, num = cost, i

print(num, min_cost)