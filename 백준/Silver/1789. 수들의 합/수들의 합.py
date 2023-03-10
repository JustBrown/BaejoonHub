S = int(input())
N = 0
count = 0
for n in range(1, S+1):
    N += n
    count += 1
    if N >= S:
        break
if N != S:
    count -= 1
print(count)