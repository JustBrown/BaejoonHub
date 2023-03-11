N, L = map(int, input().split())
H = list(map(int, input().split()))
for h in sorted(H):
    if L >= h:
        L += 1
    else:
        break
print(L)