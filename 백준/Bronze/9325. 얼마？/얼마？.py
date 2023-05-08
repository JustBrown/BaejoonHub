import sys
input = sys.stdin.readline

for _ in range(int(input())):
    result = int(input())
    for _ in range(int(input())):
        q, p = map(int, input().split())
        result += q*p
    print(result)