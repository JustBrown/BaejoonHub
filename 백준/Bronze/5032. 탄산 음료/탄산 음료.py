e, f, c = map(int, input().split())
result, empty_b = 0, e+f
while empty_b//c>0: result, empty_b = result+empty_b//c, empty_b%c+empty_b//c
print(result)