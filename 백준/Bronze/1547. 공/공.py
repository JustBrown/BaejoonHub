import sys
input = sys.stdin.readline

cups = [i+1 for i in range(3)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    x_idx, y_idx = cups.index(x), cups.index(y)
    cups[x_idx], cups[y_idx] = cups[y_idx], cups[x_idx]
print(cups[0])