import sys
input = sys.stdin.readline

def deci2bin(A, n):
    result = []
    while A != 0:
        result.append(A%n)
        A //= n
    return result[::-1]

def isPalindrom(target):
    if len(target) <= 1:
        return 1
    else:
        if target[0] == target[-1]:
            return isPalindrom(target[1:-1])
        else:
            return 0

for _ in range(int(input())):
    A, n = map(int, input().split())
    print(isPalindrom(deci2bin(A, n)))