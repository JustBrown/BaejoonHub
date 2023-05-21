import sys
input = sys.stdin.readline

i = 0
while True:
    a, op, b = input().split()
    if op=='E': break
    
    i += 1
    a, b = int(a), int(b)
    if op=='>':
        print(f'Case {i}:', 'true' if a>b else 'false')
    elif op=='>=':
        print(f'Case {i}:', 'true' if a>=b else 'false')
    elif op=='<':
        print(f'Case {i}:', 'true' if a<b else 'false')
    elif op=='<=':
        print(f'Case {i}:', 'true' if a<=b else 'false')
    elif op=='==':
        print(f'Case {i}:', 'true' if a==b else 'false')
    elif op=='!=':
        print(f'Case {i}:', 'true' if a!=b else 'false')