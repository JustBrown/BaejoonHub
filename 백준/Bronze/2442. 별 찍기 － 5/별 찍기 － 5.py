n = int(input())
print('\n'.join(' '*(n-i) + '*'*(2*i-1) for i in range(1, n+1)))