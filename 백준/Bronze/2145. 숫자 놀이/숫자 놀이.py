import sys
input = sys.stdin.readline

while True:
    n = input()[:-1]
    if n=='0':
        break
    while len(n)!=1:
        n = str(sum(list(map(int, n))))
    print(n)