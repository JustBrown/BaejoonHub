import sys
input = sys.stdin.readline

result = 1
for _ in range(int(input())):
    result += int(input())-1

print(result)