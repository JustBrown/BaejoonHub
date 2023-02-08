import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    feed = list(map(int, input().split()))
    result = 1
    while True:
        if sum(feed) > N:
            print(result)
            break
        result += 1
        feed = [feed[i] + feed[i-1 if i-1!=-1 else 5] + feed[(i+1)%6] + feed[(i+3)%6] for i in range(6)]