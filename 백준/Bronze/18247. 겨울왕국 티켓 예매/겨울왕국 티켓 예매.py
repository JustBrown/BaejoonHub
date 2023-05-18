for _ in range(int(input())):
    n, m = map(int, input().split())
    print(-1 if n<12 or m<4 else 11*m + 4)