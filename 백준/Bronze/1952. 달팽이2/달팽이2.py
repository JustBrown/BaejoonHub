m, n = map(int, input().split())
print(2*(min(m,n)-1) if m<=n else 2*min(m,n)-1)