n = int(input())
seats = [False for _ in range(101)]
result = 0
for number in map(int, input().split()):
    if not seats[number]:
        seats[number] = True
    else:
        result += 1

print(result)