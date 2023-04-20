import sys 
input = sys.stdin.readline

for _ in range(int(input())):
    lecture = int(input())
    for t in range(101):
        if t*(t+1) > lecture:
            print(t-1)
            break