n = int(input()) 
d, candidate, count = 0, [], 0
for i in range(n):
    if i == 0: d = int(input())
    else: candidate.append(int(input()))
candidate.sort(reverse=True)

if candidate:
    while d <= candidate[0]:
        candidate[0] -= 1
        d += 1
        candidate.sort(reverse=True)
        count += 1
print(count)