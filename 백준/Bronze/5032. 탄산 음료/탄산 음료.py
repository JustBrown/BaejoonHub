e, f, c = map(int, input().split())

result = 0
empty_b = e+f
while empty_b//c>0:
    result += empty_b//c
    empty_b = empty_b%c + empty_b//c

print(result)