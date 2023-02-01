import sys
input = sys.stdin.readline
array = [tuple(map(int, input().split())) for _ in range(int(input()))]
print(array.index(sorted(array, key=lambda x:(-x[0], x[1], x[2]))[0])+1)