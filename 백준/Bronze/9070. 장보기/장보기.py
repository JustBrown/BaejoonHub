import sys
input = sys.stdin.readline

for _ in range(int(input())):
    array = []
    for _ in range(int(input())):
        w, c = map(int, input().split())
        array.append((c/w, c))
    array.sort()
    print(array[0][1])