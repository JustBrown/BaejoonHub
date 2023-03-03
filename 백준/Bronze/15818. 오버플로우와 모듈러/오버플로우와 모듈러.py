n, m = map(int, input().split())
result = 1
for a in map(lambda x:int(x)%m, input().split()):
    result = result*a%m
print(result)