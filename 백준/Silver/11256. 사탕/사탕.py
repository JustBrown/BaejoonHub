T = int(input())
J, N = [], []
for i in range(T):
    j, n = map(int, input().split())
    J.append(j)
    temp = []
    for _ in range(n):
        r,c = map(int, input().split())
        temp.append(r*c)
    temp.sort(reverse=True)
    N.append(temp)

for i in range(T):
    count = 0
    for size in N[i]:
        J[i] -= size
        count += 1
        if J[i] <= 0:
            break
    print(count)