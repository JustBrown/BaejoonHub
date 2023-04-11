n = int(input())
tickets = sorted(map(int, input().split()))

cnt = 1
for ticket in tickets:
    if cnt < ticket:
        break
    cnt += 1

print(cnt)