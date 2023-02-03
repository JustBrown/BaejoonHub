import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    input()
    n, m = map(int, input().split())
    sejun = sorted(map(int, input().split()))
    sebi = sorted(map(int, input().split()))
    
    i, j = 0, 0
    while i<n and j<m:
        if sejun[i] < sebi[j]:
            i+=1
            continue
        else:
            j+=1

    print('S' if i<n else 'B')