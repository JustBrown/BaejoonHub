n = input()
result = 'NO'
for i in range(1, len(n)):
    front, back = 1, 1
    for f in map(int, n[:i]):
        front *= f
    for b in map(int, n[i:]):
        back *= b
    if front == back:
        result = 'YES'
        break
print(result)