n = int(input())
f, b = n-1, n-1
for i in range(n):
    print(''.join('*' if (j==f or j==b or i==n-1) else ' ' for j in range(b+1)))
    f, b = f-1, b+1