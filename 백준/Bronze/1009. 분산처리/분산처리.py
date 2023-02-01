import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    a, b = map(int, input().split())
    result = 1
    for _ in range(b):
        result *= a
        result%=10
    print(result if result!=0 else 10)