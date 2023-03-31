n = int(input())
name = input()
print(sum([ord(c)-64 for c in name]))