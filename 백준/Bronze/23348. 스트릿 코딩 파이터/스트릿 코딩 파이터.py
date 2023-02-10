import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
max_score = 0
for _ in range(int(input())):
    score = 0
    for _ in range(3):
        x, y, z = map(int, input().split())
        score += a*x + b*y + c*z
    if max_score < score:
        max_score = score

print(max_score)