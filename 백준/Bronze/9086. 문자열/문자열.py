import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = input()[:-1]
    print(string[0]+string[-1])