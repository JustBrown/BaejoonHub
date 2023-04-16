n = int(input())
for i in range(n):
    if i==0 or i==n-1:
        print('*'*n)
    else:
        print(''.join('*' if j==0 or j==n-1 or j==i or i+j==n-1 else ' ' for j in range(n)))