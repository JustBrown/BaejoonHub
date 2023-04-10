n, k = map(int, input().split())

result = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2)
            if str(k) in time:
                result += 1

print(result)
