n = int(input())
[print(' '*(n-i)+'*'*i if i<=n else ' '*(i-n)+'*'*(2*n-i)) for i in range(1, 2*n)]