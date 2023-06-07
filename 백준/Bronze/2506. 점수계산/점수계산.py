n = int(input())
errata = list(map(int, input().split()))
scores = [0 for _ in range(n)]

isPreRight = False
for i in range(n):
    if i==0:
        scores[0] = 1 if errata[0]==1 else 0
        isPreRight = True if errata[0]==1 else False
        continue
    
    scores[i], isPreRight = (0, False) if errata[i]==0 else (scores[i-1]+1, True)

print(sum(scores))