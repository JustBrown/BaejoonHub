import sys
input = sys.stdin.readline

for _ in range(int(input())):
    d, n, s, p = map(int, input().split())
    paral, serial = d+n*p, n*s
    print('parallelize' if paral < serial else ('do not parallelize' if paral > serial else 'does not matter'))