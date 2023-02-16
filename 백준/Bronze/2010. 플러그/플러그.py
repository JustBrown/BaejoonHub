import sys
input = sys.stdin.readline
print(1+sum([int(input())-1 for _ in range(int(input()))]))