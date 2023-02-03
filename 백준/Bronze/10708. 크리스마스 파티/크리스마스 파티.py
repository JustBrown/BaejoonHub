import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
A = list(map(int, input().split()))
score = [0]*n
for i in range(m):
    B = list(map(int, input().split()))
    ans_num = 0
    for j in range(n):
        if B[j]==A[i]:
            score[j] += 1
            ans_num += 1
    score[A[i]-1] += n-ans_num

for s in score:
    print(s)