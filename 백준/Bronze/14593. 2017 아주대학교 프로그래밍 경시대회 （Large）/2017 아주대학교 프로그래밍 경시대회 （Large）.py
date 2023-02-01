import sys
input = sys.stdin.readline

array = []
for i in range(int(input())):
    s, c, l = map(int, input().split())
    array.append((s, -c, -l, i+1))
array.sort(reverse=True)

print(array[0][3])