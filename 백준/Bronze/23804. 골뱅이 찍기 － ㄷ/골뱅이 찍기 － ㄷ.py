n = int(input())

for i in range(5):
    if i==0 or i==4:
        [print('@'*n*5) for _ in range(n)]
    else:
        [print('@'*n) for _ in range(n)]