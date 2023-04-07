import sys
input = sys.stdin.readline

for _ in range(int(input())):
    name = input()[:-1]
    good = name.count('G') + name.count('g')
    bad = name.count('B') + name.count('b')
    good_bad = 'GOOD' if good>bad else ('NEUTRAL' if good==bad else'A BADDY')
    print(name, 'is', good_bad)