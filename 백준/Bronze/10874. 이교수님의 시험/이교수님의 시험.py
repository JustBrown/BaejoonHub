import sys
input = sys.stdin.readline

result = []
for i in range(int(input())):
    if list(map(int, input().split())) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]:
        result.append(i+1)

for r in result:
    print(r)
