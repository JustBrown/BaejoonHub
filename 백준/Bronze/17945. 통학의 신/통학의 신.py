a, b = map(int, input().split())
result = sorted(map(int, set([-a+(a**2-b)**0.5, -a-(a**2-b)**0.5])))
[print(r, end=' ') for r in result]