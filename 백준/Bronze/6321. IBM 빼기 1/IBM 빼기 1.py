import sys
input = sys.stdin.readline

for i in range(int(input())):
    name = input()[:-1]
    print(f'String #{i+1}')
    print(''.join([chr(ord(n)+1) if n!='Z' else 'A' for n in name]) + '\n')