n, k = map(int, input().split())
availables = sum(list(map(lambda x:(int(x)+1)//2, input().split())))
print('YES' if n<=availables else 'NO')