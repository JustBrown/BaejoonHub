n, k = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
print('\n'.join(' '.join(str(array[i//k][j//k]) for j in range(k*n)) for i in range(k*n)))