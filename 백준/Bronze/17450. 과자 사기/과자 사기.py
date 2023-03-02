result = []
answer = ['S', 'N', 'U']
for _ in range(3):
    c, w = map(int, input().split())
    r = c*10-500 if c*10>=5000 else c*10
    result.append(w*10/r)
print(answer[result.index(max(result))])