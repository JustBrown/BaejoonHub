import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = []
search = []
for _ in range(n):
    array.append(list(input().split()))

for _ in range(m):
    SUB, FRUIT, COLOR = input().split()
    result = 0
    for sub, fruit, color in array:
        if (SUB=='-' or sub==SUB) \
            and (FRUIT=='-' or fruit==FRUIT) \
            and (COLOR=='-' or color==COLOR):
            result += 1
    print(result)